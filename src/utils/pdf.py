## \file /src/utils/pdf.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
.. module:: src.utils.pdf 
    :platform: Windows, Unix
    :synopsis: Модуль для преобразования HTML-контента или файлов в PDF

Модуль для преобразования HTML-контента или файлов в PDF с использованием различных библиотек.
Дополнительная информация:
- https://chatgpt.com/share/672266a3-0048-800d-a97b-c38f647d496b
- https://stackoverflow.com/questions/73599970/how-to-solve-wkhtmltopdf-reported-an-error-exit-with-code-1-due-to-network-err
- https://habr.com/ru/companies/bothub/articles/853490/
"""

import sys
import os
import json

from pathlib import Path
from typing import Any
import pdfkit
from reportlab.pdfgen import canvas

import header
from header import __root__

from src.logger.logger import logger
from src.utils.printer import pprint


class PDFUtils:
    """
    Класс для работы с PDF-файлами, предоставляющий методы для сохранения HTML-контента в PDF с использованием различных библиотек.
    """

    @staticmethod
    def save_pdf_pdfkit(data: str | Path, pdf_file: str | Path) -> bool:
        """
        Сохранить HTML-контент или файл в PDF с использованием библиотеки `pdfkit`.

        Args:
            data (str | Path): HTML-контент или путь к HTML-файлу.
            pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

        Returns:
            bool: `True` если PDF успешно сохранен, иначе `False`.

        Raises:
            pdfkit.PDFKitError: Ошибка генерации PDF через `pdfkit`.
            OSError: Ошибка доступа к файлу.
        """
        wkhtmltopdf_exe = __root__ / 'bin' / 'wkhtmltopdf' / 'files' / 'bin' /  'wkhtmltopdf.exe'

        if not wkhtmltopdf_exe.exists():
            logger.error("Не найден wkhtmltopdf.exe по указанному пути.")
            raise FileNotFoundError("wkhtmltopdf.exe отсутствует")

        try:
            configuration = pdfkit.configuration(
                            wkhtmltopdf=str(wkhtmltopdf_exe)
                            )

            options = {"enable-local-file-access": ""}
            if isinstance(data, str):
                # Преобразование HTML-контента в PDF
                pdfkit.from_string(data, pdf_file, configuration=configuration, options=options)
            else:
                # Преобразование HTML-файла в PDF
                pdfkit.from_file(str(data), pdf_file, configuration=configuration, options=options)
            logger.info(f"PDF успешно сохранен: {pdf_file}")
            return True
        # except (pdfkit.PDFKitError, OSError) as ex:
        #     logger.error("Ошибка генерации PDF: ", ex)
        #     return False
        except Exception as ex:
            logger.error("Неожиданная ошибка: ", ex, False)
            ...
            return False

    @staticmethod
    def save_pdf_fpdf(data: str, pdf_file: str | Path) -> bool:
        """
        Сохранить текст в PDF с использованием библиотеки FPDF.

        Args:
            data (str): Текст, который необходимо сохранить в PDF.
            pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

        Returns:
            bool: `True`, если PDF успешно сохранен, иначе `False`.
        """
        try:
            from fpdf import FPDF
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto = True, margin = 15)

            # Путь к файлу fonts.json
            fonts_file_path = __root__ / 'assets' / 'fonts' / 'fonts.json'
            if not fonts_file_path.exists():
                logger.error(
                    f'JSON файл установки шрифтов не найден: {fonts_file_path}\n'
                    'Формат файла `fonts.json`:\n'
                    '{\n'
                    '    "dejavu-sans.book": {\n'
                    '        "family": "DejaVuSans",\n'
                    '        "path": "dejavu-sans.book.ttf",\n'
                    '        "style": "book",\n'
                    '        "uni": true\n'
                    '    }\n'
                    '}'
                )
                raise FileNotFoundError(f'Файл шрифтов не найден: {fonts_file_path}')
                ...

            with open(fonts_file_path, 'r', encoding = 'utf-8') as json_file:
                fonts = json.load(json_file)

            # Добавление шрифтов
            for font_name, font_info in fonts.items():
                font_path = __root__ / 'assets' / 'fonts' / font_info['path']
                if not font_path.exists():
                    logger.error(f'Файл шрифта не найден: {font_path}')
                    raise FileNotFoundError(f'Файл шрифта не найден: {font_path}')
                    ...

                pdf.add_font(font_info['family'], font_info['style'], str(font_path), uni = font_info['uni'])

            # Установка шрифта по умолчанию
            pdf.set_font('DejaVuSans', style = 'book', size = 12)
            pdf.multi_cell(0, 10, data)
            pdf.output(str(pdf_file))
            logger.info(f'PDF отчет успешно сохранен: {pdf_file}')
            return True
        except Exception as ex:
            logger.error('Ошибка при сохранении PDF через FPDF: ', ex)
            ...
            return False


    @staticmethod
    def save_pdf_weasyprint(data: str | Path, pdf_file: str | Path) -> bool:
        """
        Сохранить HTML-контент или файл в PDF с использованием библиотеки `WeasyPrint`.

        Args:
            data (str | Path): HTML-контент или путь к HTML-файлу.
            pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

        Returns:
            bool: `True` если PDF успешно сохранен, иначе `False`.
        """
        try:
            from weasyprint import HTML
            if isinstance(data, str):
                HTML(string=data).write_pdf(pdf_file)
            else:
                HTML(filename=str(data)).write_pdf(pdf_file)
            logger.info(f"PDF успешно сохранен: {pdf_file}")
            return True
        except Exception as ex:
            logger.error("Ошибка при сохранении PDF через WeasyPrint: ", ex)
            return False

    @staticmethod
    def save_pdf_xhtml2pdf(data: str | Path, pdf_file: str | Path) -> bool:
        """
        Сохранить HTML-контент или файл в PDF с использованием библиотеки `xhtml2pdf`.

        Args:
            data (str | Path): HTML-контент или путь к HTML-файлу.
            pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

        Returns:
            bool: `True` если PDF успешно сохранен, иначе `False`.
        """
        try:
            from xhtml2pdf import pisa
            with open(pdf_file, "w+b") as result_file:
                if isinstance(data, str):
                    # Убедимся, что строка имеет кодировку UTF-8
                    data_utf8 = data.encode('utf-8').decode('utf-8')  # Преобразуем строку обратно в UTF-8, если нужно
                    try:
                        pisa.CreatePDF(data, dest=result_file)
                    except Exception as ex:
                        logger.error("Ошибка компиляции PDF: ", ex)
                        ...
                else:
                    with open(data, "r", encoding="utf-8") as source_file:
                        try:
                            # Прочитаем файл в кодировке UTF-8
                            source_data = source_file.read()
                            pisa.CreatePDF(source_data, dest=result_file, encoding='UTF-8')
                        except Exception as ex:
                            logger.error("Ошибка компиляции PDF: ", ex)
                            ...
            logger.info(f"PDF успешно сохранен: {pdf_file}")
            ...
            return True
        except Exception as ex:
            logger.error("Ошибка при сохранении PDF через xhtml2pdf: ", ex)
            ...
            return False

    @staticmethod
    def html2pdf(html_str: str, pdf_file: str | Path) -> bool | None:
        """Converts HTML content to a PDF file using WeasyPrint."""
        try:

            from weasyprint import HTML
            HTML(string=html_str).write_pdf(pdf_file)
            return True
        except Exception as e:
            print(f"Error during PDF generation: {e}")
            return


        
    @staticmethod
    def pdf_to_html(pdf_file: str | Path, html_file: str | Path) -> bool:
        """
        Конвертирует PDF-файл в HTML-файл.

        Args:
            pdf_file (str | Path): Путь к исходному PDF-файлу.
            html_file (str | Path): Путь к сохраняемому HTML-файлу.

        Returns:
            bool: `True`, если конвертация прошла успешно, иначе `False`.
        """
        try:
            # Извлечение текста из PDF
            from pdfminer.high_level import extract_text
            text = extract_text(str(pdf_file))

            # Создание HTML-файла
            with open(html_file, 'w', encoding='utf-8') as file:
                file.write(f"<html><body>{text}</body></html>")

            print(f"HTML успешно сохранен: {html_file}")
            return True
        except Exception as ex:
            print(f"Ошибка при конвертации PDF в HTML: {ex}")
            return False

    # Функция для конвертации словаря в PDF
    @staticmethod
    def dict2pdf(data: Any, file_path: str | Path) -> None:
        """
        Save dictionary data to a PDF file.

        Args:
            data (dict | SimpleNamespace): The dictionary to convert to PDF.
            file_path (str | Path): Path to the output PDF file.
        """
        if isinstance(data, 'SimpleNamespace'):
            data = data.__dict__

        pdf = canvas.Canvas(str(file_path), pagesize=A4)
        width, height = A4
        x, y = 50, height - 50

        pdf.setFont("Helvetica", 12)

        for key, value in data.items():
            line = f"{key}: {value}"
            pdf.drawString(x, y, line)
            y -= 20

            if y < 50:  # Создать новую страницу, если места недостаточно
                pdf.showPage()
                pdf.setFont("Helvetica", 12)
                y = height - 50

        pdf.save()

