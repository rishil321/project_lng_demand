from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    market_role = models.CharField(
        max_length=100,
        choices=[("Importer", "Importer"), ("Exporter", "Exporter"), ("Both", "Both")],
    )

    class Meta:
        ordering: list[str] = ["name"]

    def __str__(self) -> str:
        return self.name


class LNGVolume(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    year = models.IntegerField()
    volume = models.FloatField(verbose_name="Volume (x 10^6 cubic meters of liquid)")
    direction = models.CharField(
        max_length=100, choices=[("Import", "Import"), ("Export", "Export")]
    )
    market_share = models.FloatField(verbose_name="Market Share In %")

    def __str__(self) -> str:
        return f"{self.country}-{self.volume}({self.year})"
