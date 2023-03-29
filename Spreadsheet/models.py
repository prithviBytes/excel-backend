from django.db import models

class Spreadsheet(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class Sheet(models.Model):
    spreadsheet = models.ForeignKey(
        Spreadsheet, on_delete=models.CASCADE, related_name="sheets"
    )
    name = models.CharField(max_length=255)
    row_count = models.IntegerField()
    column_count = models.IntegerField()


class Row(models.Model):
    sheet = models.ForeignKey(
        Sheet, on_delete=models.CASCADE, related_name="rows"
    )


class Cell(models.Model):
    row = models.ForeignKey(
        Row, on_delete=models.CASCADE, related_name="cells"
    )
    column = models.IntegerField()
    value = models.CharField(max_length=255)
    formula = models.CharField(max_length=255, blank=True, null=True)
