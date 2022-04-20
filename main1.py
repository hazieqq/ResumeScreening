#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import  pandas as pd
from tika import parser
import io, os, subprocess, code, glob, re, traceback, sys, inspect
import json, re, pickle,logging, nltk ,spacy,string ,tika ,zipfile,csv
import en_core_web_sm
nlp = spacy.load('en_core_web_lg')

doc_files = glob.glob("Resume&Job_Description/Original_Resumes/*.doc",recursive=True)
docx_files = glob.glob("resume.pdf",recursive=True)
files = set(doc_files + docx_files)
files = list(files)

print ("%d files identified" %len(files))



