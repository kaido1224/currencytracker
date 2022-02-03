# Generated by Django 3.2.9 on 2021-12-10 03:11

from django.db import migrations


class Migration(migrations.Migration):
    def populate_currency(apps, schema_editor):
        book = apps.get_model("myapp", "Book")
        currency = apps.get_model("myapp", "Currency")

        # # Create a book first.
        # book_1 = book.objects.create(
        #     description="Austin's World Currency Book"
        # )
        # book_2 = book.objects.create(
        #     description="Red World Currency Book"
        # )

        # # Populate the books with entries.
        # currency.objects.bulk_create([
        #     currency(book=book_1, page=1, row=1, column=1, currency="Franc",
        #              value=5, type="Coin", country="FR"),
        #     currency(book=book_1, page=1, row=1, column=2, currency="Franc",
        #              value=5, type="Coin", country="FR"),
        #     currency(book=book_1, page=1, row=1, column=3, currency="Peso",
        #              value=5, type="Coin", country="MX"),
        #     currency(book=book_1, page=1, row=1, column=4, currency="Colones",
        #              value=100, type="Coin", country="CR"),
        #     currency(book=book_1, page=1, row=1, column=5, currency="Drachmes",
        #              value=100, type="Coin", country="GR"),
        #     currency(book=book_1, page=1, row=2, column=1, currency="Franc",
        #              value=10, type="Coin", country="FR"),
        #     currency(book=book_1, page=1, row=2, column=2, currency="Franc",
        #              value=1, type="Coin", country="FR"),
        #     currency(book=book_1, page=1, row=2, column=3, currency="Peso",
        #              value=500, type="Coin", country="CO"),
        #     currency(book=book_1, page=1, row=2, column=4, currency="Piastres",
        #              value=10, type="Coin", country="EG"),
        #     currency(book=book_1, page=1, row=2, column=5, currency="Cent",
        #              value=2, type="Coin", country="AU"),
        #     currency(book=book_1, page=1, row=3, column=1, currency="Peso",
        #              value=100, type="Coin", country="CL"),
        #     currency(book=book_1, page=1, row=3, column=2, currency="Øre",
        #              value=5, type="Coin", country="DK"),
        #     currency(book=book_1, page=1, row=3, column=3, currency="Penny",
        #              value=1, type="Coin", country="GB"),
        #     currency(book=book_1, page=1, row=3, column=4, currency="Penny",
        #              value=1, type="Coin", country="GB"),
        #     currency(book=book_1, page=1, row=3, column=5, currency="Dollar",
        #              value=1, type="Coin", country="HK"),
        #     currency(book=book_1, page=1, row=4, column=1, currency="Øre",
        #              value=5, type="Coin", country="DK"),
        #     currency(book=book_1, page=1, row=4, column=2, currency="Peso",
        #              value=50, type="Coin", country="MX"),
        #     currency(book=book_1, page=1, row=4, column=3, currency="Cent",
        #              value=25, type="Coin", country="BZ"),
        #     currency(book=book_1, page=1, row=4, column=4, currency="Lire",
        #              value=10, type="Coin", country="IT"),
        #     currency(book=book_1, page=1, row=4, column=5, currency="Euro Cent",
        #              value=2, type="Coin", country="AT"),
        #     currency(book=book_1, page=1, row=5, column=1, currency="Pesetas",
        #              value=100, type="Coin", country="ES"),
        #     currency(book=book_1, page=1, row=5, column=2, currency="Franc",
        #              value=0.5, type="Coin", country="FR"),
        #     currency(book=book_1, page=1, row=5, column=3, currency="Centesimi",
        #              value=50, type="Coin", country="IT"),
        #     currency(book=book_1, page=1, row=5, column=4, currency="Lire",
        #              value=10, type="Coin", country="IT"),
        #     currency(book=book_1, page=1, row=5, column=5, currency="Pesetas",
        #              value=5, type="Coin", country="ES"),
        #     currency(book=book_1, page=1, row=6, column=1, currency="Penniä",
        #              value=20, type="Coin", country="FI"),
        #     currency(book=book_1, page=1, row=6, column=2, currency="Peso",
        #              value=50, type="Coin", country="MX"),
        #     currency(book=book_1, page=1, row=6, column=3, currency="Franc",
        #              value=20, type="Coin", country="FR"),
        #     currency(book=book_1, page=1, row=6, column=4, currency="Peso",
        #              value=1, type="Coin", country="MX"),
        #     currency(book=book_1, page=1, row=6, column=5, currency="Yen",
        #              value=10, type="Coin", country="JP"),
        #     currency(book=book_1, page=2, row=1, column=1, currency="Cent",
        #              value=5, type="Coin", country="LK"),
        #     currency(book=book_1, page=2, row=1, column=2, currency="Lire",
        #              value=20, type="Coin", country="IT"),
        #     currency(book=book_1, page=2, row=1, column=3, currency="Franc",
        #              value=1, type="Coin", country="FR"),
        #     currency(book=book_1, page=2, row=1, column=4, currency="Piastres",
        #              value=10, type="Coin", country="EG"),
        #     currency(book=book_1, page=2, row=1, column=5, currency="Penny",
        #              value=0.5, type="Coin", country="GB"),
        #     currency(book=book_1, page=2, row=2, column=1, currency="Agorot",
        #              value=5, type="Coin", country="IL"),
        #     currency(book=book_1, page=2, row=2, column=2, currency="??",
        #              value=None, type="Coin", country=""),
        #     currency(book=book_1, page=2, row=2, column=3, currency="Jiao",
        #              value=5, type="Coin", country="TW"),  # Taiwan
        #     currency(book=book_1, page=2, row=2, column=4, currency="Centavos",
        #              value=10, type="Coin", country="MX"),
        #     currency(book=book_1, page=2, row=2, column=5, currency="Forint",
        #              value=2, type="Coin", country="HU"),
        #     currency(book=book_1, page=2, row=3, column=1, currency="Filler",
        #              value=2, type="Coin", country="HU"),
        #     currency(book=book_1, page=2, row=3, column=2, currency="Centavos",
        #              value=5, type="Coin", country="DO"),
        #     currency(book=book_1, page=2, row=3, column=3, currency="Franc",
        #              value=0.5, type="Coin", country="FR"),
        #     currency(book=book_1, page=2, row=3, column=4, currency="Franc",
        #              value=1, type="Coin", country="FR"),
        #     currency(book=book_1, page=2, row=3, column=5, currency="Centimes",
        #              value=10, type="Coin", country="HT"),
        #     currency(book=book_1, page=2, row=4, column=1, currency="Centimes",
        #              value=10, type="Coin", country="FR"),
        #     currency(book=book_1, page=2, row=4, column=2, currency="Dollar",
        #              value=1, type="Coin", country="HK"),
        #     currency(book=book_1, page=2, row=4, column=3, currency="Franc",
        #              value=5, type="Coin", country="LU"),
        #     currency(book=book_1, page=2, row=4, column=4, currency="Krona",
        #              value=1, type="Coin", country="SE"),
        #     currency(book=book_1, page=2, row=4, column=5, currency="Kobo",
        #              value=10, type="Coin", country="NG"),
        #     currency(book=book_1, page=2, row=5, column=1, currency="Peso",
        #              value=1, type="Coin", country="MX"),
        #     currency(book=book_1, page=2, row=5, column=2, currency="Centavos",
        #              value=20, type="Coin", country="CO"),
        #     currency(book=book_1, page=2, row=5, column=3, currency="Franc",
        #              value=1, type="Coin", country="FR"),
        #     currency(book=book_1, page=2, row=5, column=4, currency="Lire",
        #              value=5, type="Coin", country="IT"),
        #     currency(book=book_1, page=2, row=5, column=5, currency="Franc",
        #              value=1, type="Coin", country="FR"),
        #     currency(book=book_1, page=2, row=6, column=1, currency="Centavos",
        #              value=5, type="Coin", country="MX"),
        #     currency(book=book_1, page=2, row=6, column=2, currency="Penny",
        #              value=1, type="Coin", country="GB"),
        #     currency(book=book_1, page=2, row=6, column=3, currency="Penny",
        #              value=1, type="Coin", country="GB"),
        #     currency(book=book_1, page=2, row=6, column=4, currency="Yen",
        #              value=1, type="Coin", country="JP"),
        #     currency(book=book_1, page=2, row=6, column=5, currency="Cent",
        #              value=5, type="Coin", country="BS"),
        #     currency(book=book_1, page=3, row=1, column=1, currency="Penniä",
        #              value=10, type="Coin", country="FI"),
        #     currency(book=book_1, page=3, row=1, column=2, currency="Cent",
        #              value=1, type="Coin", country="BS"),
        #     currency(book=book_1, page=3, row=1, column=3, currency="Lire",
        #              value=20, type="Coin", country="IT"),
        #     currency(book=book_1, page=3, row=1, column=4, currency="Sengi",
        #              value=10, type="Coin", country="CD"),
        #     currency(book=book_1, page=3, row=1, column=5, currency="Centimes",
        #              value=10, type="Coin", country="FR"),
        #     currency(book=book_1, page=3, row=2, column=1, currency="Centimes",
        #              value=5, type="Coin", country="FR"),
        #     currency(book=book_1, page=3, row=2, column=2, currency="Stotinki",
        #              value=1, type="Coin", country="BG"),
        #     currency(book=book_1, page=3, row=2, column=3, currency="Shilling",
        #              value=1, type="Coin", country="IE"),
        #     currency(book=book_1, page=3, row=2, column=4, currency="Paise",
        #              value=3, type="Coin", country="IN"),
        #     currency(book=book_1, page=3, row=2, column=5, currency="Centesimos",
        #              value=5, type="Coin", country="CL"),
        #     currency(book=book_1, page=3, row=3, column=1, currency="Cent",
        #              value=10, type="Coin", country="NL"),
        #     currency(book=book_1, page=3, row=3, column=2, currency="Koruna",
        #              value=1, type="Coin", country="CS"),
        #     currency(book=book_1, page=3, row=3, column=3, currency="Escudos",
        #              value=2.5, type="Coin", country="PT"),
        #     currency(book=book_1, page=3, row=3, column=4, currency="Centavos",
        #              value=10, type="Coin", country="DO"),
        #     currency(book=book_1, page=3, row=3, column=5, currency="Cent",
        #              value=5, type="Coin", country="NL"),
        #     currency(book=book_1, page=3, row=4, column=1, currency="Franc",
        #              value=1, type="Coin", country="BE"),
        #     currency(book=book_1, page=3, row=4, column=2, currency="Centavos",
        #              value=10, type="Coin", country="BR"),
        #     currency(book=book_1, page=3, row=4, column=3, currency="Groschen",
        #              value=10, type="Coin", country="AT"),
        #     currency(book=book_1, page=3, row=4, column=4, currency="Centimes",
        #              value=50, type="Coin", country="BE"),
        #     currency(book=book_1, page=3, row=4, column=5, currency="Pfennig",
        #              value=1, type="Coin", country="DE"),
        #     currency(book=book_1, page=3, row=5, column=1, currency="Franc",
        #              value=10, type="Coin", country="FR"),
        #     currency(book=book_1, page=3, row=5, column=2, currency="Pice",
        #              value=1, type="Coin", country="IN"),
        #     currency(book=book_1, page=3, row=5, column=3, currency="Cent",
        #              value=2, type="Coin", country="ZA"),
        #     currency(book=book_1, page=3, row=5, column=4, currency="Farthing",
        #              value=1, type="Coin", country="GB"),
        #     currency(book=book_1, page=3, row=5, column=5, currency="Centavos",
        #              value=10, type="Coin", country="BR"),
        #     currency(book=book_1, page=3, row=6, column=1, currency="Pfennig",
        #              value=5, type="Coin", country="DE"),
        #     currency(book=book_1, page=3, row=6, column=2, currency="Cent",
        #              value=25, type="Coin", country="AW"),
        #     currency(book=book_1, page=3, row=6, column=3, currency="Fen",
        #              value=2, type="Coin", country="CN"),
        #     currency(book=book_1, page=3, row=6, column=4, currency="Cruzeiro",
        #              value=1, type="Coin", country="BR"),
        #     currency(book=book_1, page=3, row=6, column=5, currency="Cent",
        #              value=10, type="Coin", country="CE"),
        #     currency(book=book_1, page=4, row=1, column=1, currency="Koruna",
        #              value=1, type="Coin", country="CS"),
        #     currency(book=book_1, page=4, row=1, column=2, currency="Centimes",
        #              value=5, type="Coin", country="FR"),
        #     currency(book=book_1, page=4, row=1, column=3, currency="Rappen",
        #              value=5, type="Coin", country="CH"),
        #     currency(book=book_1, page=4, row=1, column=4, currency="Kopek",
        #              value=10, type="Coin", country="SU"),
        #     currency(book=book_1, page=4, row=1, column=5, currency="Øre",
        #              value=25, type="Coin", country="NO"),
        #     currency(book=book_1, page=4, row=2, column=1, currency="Euro Cent",
        #              value=2, type="Coin", country="IE"),
        #     currency(book=book_1, page=4, row=2, column=2, currency="Centavos",
        #              value=5, type="Coin", country="MX"),
        #     currency(book=book_1, page=4, row=2, column=3, currency="Aurar",
        #              value=10, type="Coin", country="IS"),
        #     currency(book=book_1, page=4, row=2, column=4, currency="Kopek",
        #              value=2, type="Coin", country="SU"),
        #     currency(book=book_1, page=4, row=2, column=5, currency="Santims",
        #              value=1, type="Coin", country="LV"),
        #     currency(book=book_1, page=4, row=3, column=1, currency="Cent",
        #              value=25, type="Coin", country="NL"),
        #     currency(book=book_1, page=4, row=3, column=2, currency="Centimos",
        #              value=25, type="Coin", country="CR"),
        #     currency(book=book_1, page=4, row=3, column=3, currency="Centimes",
        #              value=25, type="Coin", country="BE"),
        #     currency(book=book_1, page=4, row=3, column=4, currency="Cent",
        #              value=1, type="Coin", country="CA"),
        #     currency(book=book_1, page=4, row=3, column=5, currency="Cent",
        #              value=1, type="Coin", country="GB"),
        #     currency(book=book_1, page=4, row=4, column=1, currency="Cent",
        #              value=5, type="Coin", country="CA"),
        #     currency(book=book_1, page=4, row=4, column=2, currency="Grosz",
        #              value=1, type="Coin", country="PL"),
        #     currency(book=book_1, page=4, row=4, column=3, currency="Sen",
        #              value=10, type="Coin", country="MY"),
        #     currency(book=book_1, page=4, row=4, column=4, currency="Dollar",
        #              value=1, type="Coin", country="US"),
        #     currency(book=book_1, page=4, row=4, column=5, currency="Franc",
        #              value=1, type="Coin", country="BE"),
        #     currency(book=book_1, page=4, row=5, column=1, currency="Cent",
        #              value=5, type="Coin", country="CA"),
        #     currency(book=book_1, page=4, row=5, column=2, currency="Pfennig",
        #              value=10, type="Coin", country="DE"),
        #     currency(book=book_1, page=4, row=5, column=3, currency="Yen",
        #              value=10, type="Coin", country="JP"),
        #     currency(book=book_1, page=4, row=5, column=4, currency="Mark",
        #              value=2, type="Coin", country="DE"),
        #     currency(book=book_1, page=4, row=5, column=5, currency="Guarani",
        #              value=1, type="Coin", country="PY"),
        #     currency(book=book_1, page=4, row=6, column=1, currency="Pfennig",
        #              value=1, type="Coin", country="DE"),
        #     currency(book=book_1, page=4, row=6, column=2, currency="Pfennig",
        #              value=1, type="Coin", country="DE"),
        #     currency(book=book_1, page=4, row=6, column=3, currency="Cent",
        #              value=10, type="Coin", country="CA"),
        #     currency(book=book_1, page=4, row=6, column=4, currency="Penny",
        #              value=1, type="Coin", country="GB"),
        #     currency(book=book_1, page=4, row=6, column=5, currency="Pfennig",
        #              value=50, type="Coin", country="DE"),
        #     currency(book=book_1, page=5, row=1, column=1, currency="Kuruş",
        #              value=10, type="Coin", country="TR"),
        #     currency(book=book_1, page=5, row=1, column=2, currency="Rials",
        #              value=500, type="Coin", country="IR"),
        #     currency(book=book_1, page=5, row=1, column=3, currency="Rials",
        #              value=1000, type="Coin", country="IR"),
        #     currency(book=book_1, page=5, row=1, column=4, currency="Rials",
        #              value=5000, type="Coin", country="IR"),
        #     currency(book=book_1, page=5, row=1, column=5, currency="Grosz",
        #              value=1, type="Coin", country="PL"),
        #     currency(book=book_1, page=5, row=2, column=1, currency="Hellers",
        #              value=10, type="Coin", country="CS"),
        #     currency(book=book_1, page=5, row=2, column=2, currency="Groschen",
        #              value=5, type="Coin", country="AT"),
        #     currency(book=book_1, page=5, row=2, column=3, currency="Forint",
        #              value=5, type="Coin", country="HU"),
        #     currency(book=book_1, page=5, row=2, column=4, currency="Pfennig",
        #              value=2, type="Coin", country="DE"),
        #     currency(book=book_1, page=5, row=2, column=5, currency="Stotinki",
        #              value=5, type="Coin", country="BG"),
        #     currency(book=book_1, page=5, row=3, column=1, currency="Penny",
        #              value=0.5, type="Coin", country="GB"),
        #     currency(book=book_1, page=5, row=3, column=2, currency="Lipa",
        #              value=5, type="Coin", country="HR"),
        #     currency(book=book_1, page=5, row=3, column=3, currency="Lire",
        #              value=100, type="Coin", country="IT"),
        #     currency(book=book_1, page=5, row=3, column=4, currency="Pesetas",
        #              value=10, type="Coin", country="ES"),
        #     currency(book=book_1, page=5, row=3, column=5, currency="Øre",
        #              value=25, type="Coin", country="SE"),
        #     currency(book=book_1, page=5, row=4, column=1, currency="Kuruş",
        #              value=10, type="Coin", country="TR"),
        #     currency(book=book_1, page=5, row=4, column=2, currency="Cent",
        #              value=10, type="Coin", country="ZA"),
        #     currency(book=book_1, page=5, row=4, column=3, currency="Dinar",
        #              value=1, type="Coin", country="YU"),
        #     currency(book=book_1, page=5, row=4, column=4, currency="Yen",
        #              value=1, type="Coin", country="JP"),
        #     currency(book=book_1, page=5, row=4, column=5, currency="Franc",
        #              value=1, type="Coin", country="BE"),
        #     currency(book=book_1, page=5, row=5, column=1, currency="Cent",
        #              value=1, type="Coin", country="CA"),
        #     currency(book=book_1, page=5, row=5, column=2, currency="Jiao",
        #              value=1, type="Coin", country="CN"),
        #     currency(book=book_1, page=5, row=5, column=3, currency="Kopek",
        #              value=1, type="Coin", country="RU"),
        #     currency(book=book_1, page=5, row=5, column=4, currency="Kopek",
        #              value=10, type="Coin", country="SU"),
        #     currency(book=book_1, page=5, row=5, column=5, currency="Cent",
        #              value=1, type="Coin", country="NE"),
        #     currency(book=book_1, page=5, row=6, column=1, currency="Bani",
        #              value=5, type="Coin", country="RO"),
        #     currency(book=book_1, page=5, row=6, column=2, currency="Escudos",
        #              value=2.5, type="Coin", country="PT"),
        #     currency(book=book_1, page=5, row=6, column=3, currency="Centimes",
        #              value=20, type="Coin", country="FR"),
        #     currency(book=book_1, page=5, row=6, column=4, currency="Cent",
        #              value=5, type="Coin", country="SG"),
        #     currency(book=book_1, page=5, row=6, column=5, currency="Sen",
        #              value=10, type="Coin", country="MY"),
        #     currency(book=book_1, page=6, row=1, column=1, currency="Penniä",
        #              value=5, type="Coin", country="FI"),
        #     currency(book=book_1, page=6, row=1, column=2, currency="Øre",
        #              value=10, type="Coin", country="DK"),
        #     currency(book=book_1, page=6, row=1, column=3, currency="Euro Cent",
        #              value=2, type="Coin", country="FR"),
        # currency(book=book_1, page=6, row=1, column=4, currency="Cent",
        #              value=50, type="Coin", country="AU"),
        #     currency(book=book_1, page=6, row=2, column=1, currency="Centavo",
        #              value=50, type="Coin", country="MX"),
        #     currency(book=book_1, page=6, row=2, column=2, currency="Euro Cent",
        #              value=20, type="Coin", country="FR"),
        #     currency(book=book_1, page=6, row=2, column=3, currency="Centavo",
        #              value=20, type="Coin", country="MX"),
        #     currency(book=book_1, page=6, row=2, column=4, currency="Pence",
        #              value=20, type="Coin", country="GB"),
        #     currency(book=book_1, page=6, row=3, column=1, currency="Euro Cent",
        #              value=2, type="Coin", country="DE"),
        #     currency(book=book_1, page=6, row=3, column=2, currency="Cent",
        #              value=1, type="Coin", country="CA"),
        #     currency(book=book_1, page=6, row=3, column=3, currency="Cent",
        #              value=25, type="Coin", country="CA"),
        #     currency(book=book_1, page=6, row=3, column=4, currency="Cent",
        #              value=1, type="Coin", country="GB"),
        #     currency(book=book_1, page=6, row=4, column=1, currency="Cent",
        #              value=1, type="Coin", country="GB"),
        #     currency(book=book_1, page=6, row=4, column=2, currency="Franc",
        #              value=1, type="Coin", country="BE"),
        #     currency(book=book_1, page=6, row=4, column=3, currency="Franc",
        #              value=1, type="Coin", country="BE"),
        #     currency(book=book_1, page=6, row=4, column=4, currency="Centime",
        #              value=25, type="Coin", country="BE"),
        #     currency(book=book_1, page=6, row=5, column=1, currency="Peso",
        #              value=10, type="Coin", country="PH"),
        #     currency(book=book_1, page=6, row=5, column=2, currency="Peso",
        #              value=5, type="Coin", country="PH"),
        #     currency(book=book_1, page=6, row=5, column=3, currency="Peso",
        #              value=1, type="Coin", country="PH"),
        #     currency(book=book_1, page=6, row=5, column=4, currency="Rappen",
        #              value=20, type="Coin", country="CH"),
        #     currency(book=book_1, page=7, row=1, column=1, currency="Rappen",
        #              value=10, type="Coin", country="CH"),
        #     currency(book=book_1, page=7, row=1, column=3, currency="Yen",
        #              value=10, type="Coin", country="JP"),
        #     currency(book=book_1, page=7, row=1, column=4, currency="Sen",
        #              value=10, type="Coin", country="MY"),
        #     currency(book=book_1, page=7, row=2, column=1, currency="Dollar",
        #              value=1, type="Coin", country="HK"),
        #     currency(book=book_1, page=7, row=2, column=1, currency="Bhat",
        #              value=10, type="Coin", country="TH"),
        #     currency(book=book_1, page=7, row=2, column=3, currency="Cent",
        #              value=25, type="Coin", country="KY"),
        #     currency(book=book_1, page=7, row=2, column=4, currency="Cent",
        #              value=10, type="Coin", country="KY"),
        #     currency(book=book_1, page=7, row=3, column=1, currency="Cent",
        #              value=5, type="Coin", country="AW"),
        #     currency(book=book_1, page=7, row=3, column=2, currency="Cent",
        #              value=25, type="Coin", country="AW"),
        #     currency(book=book_1, page=7, row=3, column=3, currency="Florin",
        #              value=1, type="Coin", country="AW"),
        #     currency(book=book_1, page=7, row=3, column=4, currency="Rupiah",
        #              value=1000, type="Coin", country="ID"),
        #     currency(book=book_1, page=7, row=4, column=1, currency="Rupiah",
        #              value=500, type="Coin", country="ID"),
        #     currency(book=book_1, page=7, row=4, column=2, currency="Rupiah",
        #              value=200, type="Coin", country="ID"),
        #     currency(book=book_1, page=7, row=4, column=3, currency="Cent",
        #              value=50, type="Coin", country="AU"),
        #     currency(book=book_1, page=7, row=4, column=4, currency="Dollar",
        #              value=1, type="Coin", country="AU"),
        #     currency(book=book_1, page=7, row=5, column=1, currency="Cent",
        #              value=10, type="Coin", country="AU"),
        #     currency(book=book_1, page=7, row=5, column=2, currency="Cent",
        #              value=20, type="Coin", country="FJ"),
        #     currency(book=book_1, page=7, row=5, column=3, currency="Cent",
        #              value=10, type="Coin", country="FJ"),
        #     currency(book=book_1, page=7, row=5, column=4, currency="Cent",
        #              value=5, type="Coin", country="FJ"),
        #     currency(book=book_1, page=8, row=1, column=1, currency="Vatu",
        #              value=100, type="Coin", country="VU"),
        #     currency(book=book_1, page=8, row=1, column=2, currency="Vatu",
        #              value=20, type="Coin", country="VU"),
        #     currency(book=book_1, page=8, row=1, column=3, currency="Vatu",
        #              value=10, type="Coin", country="VU"),
        #     currency(book=book_2, page=1, row=1, column=1, currency="Avos",
        #              value=10, type="Coin", country="MO"),
        #     currency(book=book_2, page=1, row=1, column=2, currency="Cent",
        #              value=20, type="Coin", country="HK"),
        #     currency(book=book_2, page=1, row=1, column=3, currency="Cent",
        #              value=10, type="Coin", country="HK"),
        #     currency(book=book_2, page=1, row=1, column=4, currency="Jiao",
        #              value=1, type="Coin", country="TW"),
        #     currency(book=book_2, page=1, row=1, column=5, currency="Jiao",
        #              value=1, type="Coin", country="CN"),
        #     currency(book=book_2, page=1, row=2, column=1, currency="Rupee",
        #              value=1, type="Coin", country="PK"),
        #     currency(book=book_2, page=1, row=2, column=2, currency="Paise",
        #              value=50, type="Coin", country="IN"),
        #     currency(book=book_2, page=1, row=2, column=3, currency="Satang",
        #              value=1, type="Coin", country="TH"),
        #     currency(book=book_2, page=1, row=2, column=4, currency="Chon",
        #              value=1, type="Coin", country="KP"),
        #     currency(book=book_2, page=1, row=2, column=5, currency="Won",
        #              value=10, type="Coin", country="KR"),
        #     currency(book=book_2, page=1, row=3, column=1, currency="Sen",
        #              value=10, type="Coin", country="MY"),
        #     currency(book=book_2, page=1, row=3, column=2, currency="Sen",
        #              value=20, type="Coin", country="MY"),
        #     currency(book=book_2, page=1, row=3, column=3, currency="Cent",
        #              value=5, type="Coin", country="SG"),
        #     currency(book=book_2, page=1, row=3, column=4, currency="Rupiah",
        #              value=50, type="Coin", country="ID"),
        #     currency(book=book_2, page=1, row=3, column=5, currency="Rupee",
        #              value=25, type="Coin", country="LK"),
        #     currency(book=book_2, page=1, row=4, column=1, currency="So'm",
        #              value=50, type="Coin", country="UZ"),
        #     currency(book=book_2, page=1, row=4, column=2, currency="Tenge",
        #              value=1, type="Coin", country="KZ"),
        #     currency(book=book_2, page=1, row=4, column=3, currency="Tyiyn",
        #              value=50, type="Coin", country="KG"),
        #     currency(book=book_2, page=1, row=4, column=4, currency="Tetri",
        #              value=2, type="Coin", country="GE"),
        #     currency(book=book_2, page=1, row=4, column=5, currency="Kopek",
        #              value=1, type="Coin", country="RU"),
        #     currency(book=book_2, page=2, row=1, column=1, currency="Shilling",
        #              value=1, type="Coin", country="SO"),
        #     currency(book=book_2, page=2, row=1, column=2, currency="Cent",
        #              value=10, type="Coin", country="ZA"),
        #     currency(book=book_2, page=2, row=1, column=3, currency="Franc",
        #              value=1, type="Coin", country="RW"),
        #     currency(book=book_2, page=2, row=1, column=4, currency="Qirsh",
        #              value=5, type="Coin", country="EG"),
        #     currency(book=book_2, page=2, row=1, column=5, currency="Kuruş",
        #              value=1, type="Coin", country="TR"),
        #     currency(book=book_2, page=2, row=2, column=1, currency="Tetri",
        #              value=1, type="Coin", country="GE"),
        #     currency(book=book_2, page=2, row=2, column=2, currency="Ban",
        #              value=1, type="Coin", country="RO"),
        #     currency(book=book_2, page=2, row=2, column=3, currency="Euro Cent",
        #              value=1, type="Coin", country="DE"),
        #     currency(book=book_2, page=2, row=2, column=4, currency="Kopek",
        #              value=5, type="Coin", country="RU"),
        #     currency(book=book_2, page=2, row=2, column=5, currency="Kopek",
        #              value=10, type="Coin", country="RU"),
        #     currency(book=book_2, page=2, row=3, column=1, currency="Stotinki",
        #              value=1, type="Coin", country="BG"),
        #     currency(book=book_2, page=2, row=3, column=2, currency="Euro Cent",
        #              value=1, type="Coin", country="SI"),
        #     currency(book=book_2, page=2, row=3, column=3, currency="Grosze",
        #              value=2, type="Coin", country="PL"),
        #     currency(book=book_2, page=2, row=3, column=4, currency="Euro Cent",
        #              value=1, type="Coin", country="EE"),
        #     currency(book=book_2, page=2, row=3, column=5, currency="Kopiika",
        #              value=1, type="Coin", country="UA"),
        #     currency(book=book_2, page=2, row=4, column=1, currency="Penny",
        #              value=1, type="Coin", country="GB"),
        #     currency(book=book_2, page=2, row=4, column=2, currency="Kopiika",
        #              value=10, type="Coin", country="UA"),
        #     currency(book=book_2, page=2, row=4, column=3, currency="Ruble",
        #              value=1, type="Coin", country="BY"),
        #     currency(book=book_2, page=2, row=4, column=4, currency="Euro Cent",
        #              value=1, type="Coin", country="LT"),
        #     currency(book=book_2, page=2, row=4, column=5, currency="Grosze",
        #              value=1, type="Coin", country="PL"),
        #     currency(book=book_2, page=3, row=1, column=1, currency="Euro Cent",
        #              value=1, type="Coin", country="GR"),
        #     currency(book=book_2, page=3, row=1, column=2, currency="Euro Cent",
        #              value=2, type="Coin", country="ES"),
        #     currency(book=book_2, page=3, row=1, column=3, currency="Grosze",
        #              value=10, type="Coin", country="PL"),
        #     currency(book=book_2, page=3, row=1, column=4, currency="Euro Cent",
        #              value=1, type="Coin", country="PT"),
        #     currency(book=book_2, page=3, row=1, column=5, currency="Euro Cent",
        #              value=1, type="Coin", country="AT"),
        #     currency(book=book_2, page=3, row=2, column=1, currency="Penny",
        #              value=0.5, type="Coin", country="GB"),
        #     currency(book=book_2, page=3, row=2, column=2, currency="Penny",
        #              value=1, type="Coin", country="GB"),
        #     currency(book=book_2, page=3, row=2, column=3, currency="Penny",
        #              value=1, type="Coin", country="GB"),
        #     currency(book=book_2, page=3, row=2, column=4, currency="Euro Cent",
        #              value=1, type="Coin", country="IE"),
        #     currency(book=book_2, page=3, row=2, column=5, currency="Bani",
        #              value=5, type="Coin", country="MD"),
        #     currency(book=book_2, page=3, row=3, column=1, currency="Cruzeiro",
        #              value=10, type="Coin", country="BR"),
        #     currency(book=book_2, page=3, row=3, column=2, currency="Cent",
        #              value=5, type="Coin", country="CA"),
        #     currency(book=book_2, page=3, row=3, column=3, currency="Centavos",
        #              value=5, type="Coin", country="MX"),
        #     currency(book=book_2, page=3, row=3, column=4, currency="Cent",
        #              value=1, type="Coin", country="CA"),
        #     currency(book=book_2, page=3, row=3, column=5, currency="Cent",
        #              value=1, type="Coin", country="US"),
        #     currency(book=book_2, page=3, row=4, column=1, currency="Centimos",
        #              value=5, type="Coin", country="PE"),
        #     currency(book=book_2, page=3, row=4, column=2, currency="Seniti",
        #              value=5, type="Coin", country="TO"),
        #     currency(book=book_2, page=3, row=4, column=3, currency="Cent",
        #              value=1, type="Coin", country="CK"),
        #     currency(book=book_2, page=3, row=4, column=4, currency="Toea",
        #              value=1, type="Coin", country="PG"),
        #     currency(book=book_2, page=3, row=4, column=5, currency="Cent",
        #              value=5, type="Coin", country="AU"),
        # ])

    def unpopulate_currency(apps, schema_editor):
        book = apps.get_model("myapp", "Book")

        # This will delete all of the related currency as well.
        book.objects.all().delete()

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_currency, unpopulate_currency),
    ]
