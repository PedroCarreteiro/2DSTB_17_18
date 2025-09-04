import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import Livro, Autor, Editora

class Command (BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--arquivo", default="population/livros_novo.csv")
        #Truncate apaga tudo e insere tudo depois
        parser.add_argument("-truncate", action="store_true")
        parser.add_argument("-update", action="store_true")

    @transaction.atomic
    def handle(self, *a, **o):
        df = pd.read_csv(o["arquivo"], encoding="utf-8-sig")
        df.columns = [c.strip().lower().lstrip("\ufeff") for c in df.columns]

        if o['truncate']: Livro.objects.all().delete()

        df["titulo"] = df["titulo"].astype(str).str.strip()
        df["subtitulo"] = df["subtitulo"].astype(str).str.strip()
        df["isbn"] = df["isbn"].astype(str).str.strip()
        df["descricao"] = df["descricao"].astype(str).str.strip()
        df["idioma"] = df["idioma"].astype(str).str.strip()
        df["ano_publicacao"] = df["ano_publicacao"].astype(str)
        df["paginas"] = df["paginas"].astype(int)
        df["preco"] = df["preco"].astype(float)
        df["estoque"] = df["estoque"].astype(int)
        df["desconto"] = df["desconto"].astype(float)
        df["disponivel"] = df["disponivel"].astype(bool)
        df["dimensoes"] = df["dimensoes"].astype(str).str.strip()
        df["peso"] = df["peso"].astype(float)
        df["autor"] = df["autor"].astype(int)
        df["editora"] = df["editora"].astype(int)

        df = df.query("titulo !=''")

        if o["update"]:
            criados = atualizados = 0
            for r in df.itertuples(index=False):
                # _, selecionar apenas um dos coisa do CRUD dele
                _, created = Livro.objects.update_or_create(
                    titulo=r.titulo, subtitulo=r.subtitulo, isbn=r.isbn, descricao=r.descricao, idioma=r.idioma, ano_publicacao=r.ano_publicacao, paginas=r.paginas, preco=r.preco, estoque=r.estoque, desconto=r.desconto, disponivel=r.disponivel, dimensoes=r.dimensoes, peso=r.peso, autor_id=r.autor, editora_id=r.editora
                )

                criados += int(created)
                atualizados += (not created)

            self.stdout.write(self.style.SUCCESS(f'Criados: {criados} | Atualizados: {atualizados}'))

        else:
            autor = Autor.objects.get(id=r.autor)
            editora = Editora.objects.get(id=r.editora)
            objs = [Livro(
                titulo=r.titulo, subtitulo=r.subtitulo, isbn=r.isbn, descricao=r.descricao, idioma=r.idioma, ano_publicacao=r.ano_publicacao, paginas=r.paginas, preco=r.preco, estoque=r.estoque, desconto=r.desconto, disponivel=r.disponivel, dimensoes=r.dimensoes, peso=r.peso, autor_id=autor, editora_id=editora
            ) for r in df.itertuples(index=False)]

            Livro.objects.bulk_create(objs, ignore_conflicts=True)

            self.stdout.write(self.style.SUCCESS(f'Criados: {len(objs)}'))

        