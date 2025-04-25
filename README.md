# Converter Text to CSV for "Ce spun studentii?" Show

## Introduction

This is a simple Python project I built to automate a boring task. It converts a text file containing questions and up to 8 answers with points into a clean CSV file. No manual editing, no wasted time.

It reads an `input.txt` file and spits out an `output.csv` file, structured exactly how you need it. Built this to make handling game show data way easier.

## What It Does

Reads a text file with questions and answers  
Parses each question and up to 8 answers with their points  
Exports everything neatly into a CSV file  
Handles weird formatting and missing answers without breaking

## Requirements

Python 3.6 or higher  
Any code editor (Visual Studio Code recommended)

## How the Input Looks

Example input in `input.txt`:

```
1. INTREBARE TEST 1?
—ABSDA 26
—SDASDASD 10
—ADSASDAS 21
—ADSDWEW 8
—WDASD 35

1. INTREBARE TEST 2?
—ABSDA 26
—SDASDASD 10
—ADSASDAS 21
—ADSDWEW 8
—WDASD 35
```

## What the Output CSV Looks Like

```
question,answer,points,answer,points,answer,points,answer,points,answer,points,answer,points,answer,points,answer,points
1. INTREBARE TEST 1?,WDASD,35,ADSASDAS,21,SDASDASD,10,ADSDWEW,8
1. INTREBARE TEST 2?,WDASD,35,ABSDA,26,ADSASDAS,21,SDASDASD,10,ADSDWEW,8
```

## How to Run It

### 1. Clone the repo

```bash
git clone https://github.com/DurdeuVlad/converter_text_to_csv_for_ce_spun_studentii
cd converter_text_to_csv_for_ce_spun_studentii
```

### 2. Drop your input file

Place your `input.txt` file into the project folder.

### 3. Update the script

In `txttocsv.py`, set your input file name if different.

```python
input_filename = "input.txt"
```

### 4. Run the script

```bash
python txttocsv.py
```

### 5. Done

Check your new `output.csv` file inside the project directory.

## Dependencies

Only Python 3 and the built-in `csv` module. No extra installs needed.
