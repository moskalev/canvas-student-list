#!/bin/bash
mkdir pdfs
rm pdfs/*
python getdata.py
rm pdfs/*.tex
rm pdfs/*.log
rm pdfs/*.aux
pdfunite pdfs/*.pdf pdfs/all.pdf
