from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Spreadsheet, Sheet

def create_spreadsheet_with_sheet(name, sheet_name, row_count, column_count):
    spreadsheet = Spreadsheet.objects.create(
        name=name,
        created_at=timezone.now()
    )
    sheet = Sheet.objects.create(
        spreadsheet=spreadsheet,
        name=sheet_name,
        row_count=row_count,
        column_count=column_count
    )
    return spreadsheet, sheet

def create(request):
    spreadsheet, sheet = create_spreadsheet_with_sheet("SpreadSheetName", "SheetName", 10, 10)
    return HttpResponse("Created")

def update(request):
    return HttpResponse("Success")