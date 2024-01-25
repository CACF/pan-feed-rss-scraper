#!/bin/bash

# Array containing all the CURL commands
curl_commands=(
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"AP-News\"], \"genres\": [\"Top-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"AP-News\"], \"genres\": [\"World-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"AP-News\"], \"genres\": [\"Politics\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"AP-News\"], \"genres\": [\"US-News\"]}' "
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"AP-News\"], \"genres\": [\"Sports\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"AP-News\"], \"genres\": [\"Entertainment\"]}' "
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"AP-News\"], \"genres\": [\"Business\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"AP-News\"], \"genres\": [\"Science-Technology\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"AP-News\"], \"genres\": [\"Health\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"AP-News\"], \"genres\": [\"Environment\"]}' "
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Reuters\"], \"genres\": [\"Top-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Reuters\"], \"genres\": [\"World-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Reuters\"], \"genres\": [\"African-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Reuters\"], \"genres\": [\"Americas-News\"]}' "
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Reuters\"], \"genres\": [\"Asia-Pacific-News\"]}' "
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Reuters\"], \"genres\": [\"Europe-News\"]}' "
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Reuters\"], \"genres\": [\"Indian-News\"]}' "
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Reuters\"], \"genres\": [\"Middle-East-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Reuters\"], \"genres\": [\"UK-News\"]}' "
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Reuters\"], \"genres\": [\"US-News\"]}' "
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Reuters\"], \"genres\": [\"China-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Reuters\"], \"genres\": [\"Entertainment\"]}' "
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Reuters\"], \"genres\": [\"Business\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Reuters\"], \"genres\": [\"Science-Technology\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Reuters\"], \"genres\": [\"Health\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Reuters\"], \"genres\": [\"Environment\"]}' "
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Reuters\"], \"genres\": [\"Energy\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Reuters\"], \"genres\": [\"Autos\"]}' "
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Reuters\"], \"genres\": [\"Defense-Aerospace\"]}' "
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"CNBC\"], \"genres\": [\"Top-News\"]}' "
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"CNBC\"], \"genres\": [\"World-News\"]}' "
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"CNBC\"], \"genres\": [\"Asia-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"CNBC\"], \"genres\": [\"US-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"CNBC\"], \"genres\": [\"Europe-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"CNBC\"], \"genres\": [\"Politics\"]}' "
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"CNBC\"], \"genres\": [\"Business\"]}' "
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"CNBC\"], \"genres\": [\"Technology\"]}' "
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"CNBC\"], \"genres\": [\"Travel\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"CNBC\"], \"genres\": [\"Health\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"CNBC\"], \"genres\": [\"Real-Estate\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"CNBC\"], \"genres\": [\"Autos\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"CNBC\"], \"genres\": [\"Energy\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"CNBC\"], \"genres\": [\"Entertainment\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-News\"], \"genres\": [\"Top-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-News\"], \"genres\": [\"Pakistan-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-News\"], \"genres\": [\"Sindh-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-News\"], \"genres\": [\"Punjab-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-News\"], \"genres\": [\"KPK-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-News\"], \"genres\": [\"Islamabad-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-News\"], \"genres\": [\"World-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-News\"], \"genres\": [\"Sports\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-News\"], \"genres\": [\"Business\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-News\"], \"genres\": [\"Politics\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-News\"], \"genres\": [\"Entertainment\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-News\"], \"genres\": [\"Science-Technology\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-News\"], \"genres\": [\"Health\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-News\"], \"genres\": [\"Environment\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-News\"], \"genres\": [\"Wildlife\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Express-Tribune\"], \"genres\": [\"Top-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Express-Tribune\"], \"genres\": [\"Politics\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Express-Tribune\"], \"genres\": [\"Pakistan-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Express-Tribune\"], \"genres\": [\"Sindh-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Express-Tribune\"], \"genres\": [\"Punjab-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Express-Tribune\"], \"genres\": [\"Balochistan-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Express-Tribune\"], \"genres\": [\"KPK-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Express-Tribune\"], \"genres\": [\"Kashmir-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Express-Tribune\"], \"genres\": [\"Gilgat-Baltistan-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Express-Tribune\"], \"genres\": [\"World-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Express-Tribune\"], \"genres\": [\"Sports\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Express-Tribune\"], \"genres\": [\"Health\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Express-Tribune\"], \"genres\": [\"Entertainment\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Express-Tribune\"], \"genres\": [\"Business\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Express-Tribune\"], \"genres\": [\"Science-Technology\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Al-Jazeera\"], \"genres\": [\"Top-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"BBC\"], \"genres\": [\"Top-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"BBC\"], \"genres\": [\"World-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"BBC\"], \"genres\": [\"UK-news\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"BBC\"], \"genres\": [\"Business\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"BBC\"], \"genres\": [\"Politics\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"BBC\"], \"genres\": [\"Health\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"BBC\"], \"genres\": [\"Environment\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"BBC\"], \"genres\": [\"Science-Technology\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"BBC\"], \"genres\": [\"Entertainment\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"DW-News\"], \"genres\": [\"Top-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"DW-News\"], \"genres\": [\"German-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"DW-News\"], \"genres\": [\"World-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"DW-News\"], \"genres\": [\"Europe-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"DW-News\"], \"genres\": [\"Business\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"DW-News\"], \"genres\": [\"Science-Technology\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"DW-News\"], \"genres\": [\"Environment\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"DW-News\"], \"genres\": [\"Entertainment\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"DW-News\"], \"genres\": [\"Sports\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"DW-News\"], \"genres\": [\"Asia-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-Guardian\"], \"genres\": [\"Top-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-Guardian\"], \"genres\": [\"African-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-Guardian\"], \"genres\": [\"Americas-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-Guardian\"], \"genres\": [\"Asia-Pacific-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-Guardian\"], \"genres\": [\"Australian-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-Guardian\"], \"genres\": [\"Europe-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-Guardian\"], \"genres\": [\"Middle-East-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-Guardian\"], \"genres\": [\"South-And-Central-Asia-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-Guardian\"], \"genres\": [\"Bangladesh-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-Guardian\"], \"genres\": [\"Indian-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-Guardian\"], \"genres\": [\"UK-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-Guardian\"], \"genres\": [\"US-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-Guardian\"], \"genres\": [\"Ukraine-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-Guardian\"], \"genres\": [\"Environment\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-Guardian\"], \"genres\": [\"Wildlife\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-Guardian\"], \"genres\": [\"Science-Technology\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-Guardian\"], \"genres\": [\"Business\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-Guardian\"], \"genres\": [\"Health\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-Guardian\"], \"genres\": [\"Sports\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-Guardian\"], \"genres\": [\"Energy\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"The-Guardian\"], \"genres\": [\"Entertainment\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Abb Takk TV\"], \"genres\": [\"Top-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"SUCH-TV\"], \"genres\": [\"Top-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"SUCH-TV\"], \"genres\": [\"Pak-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"SUCH-TV\"], \"genres\": [\"World-News\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"SUCH-TV\"], \"genres\": [\"Business\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"SUCH-TV\"], \"genres\": [\"Sports\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"SUCH-TV\"], \"genres\": [\"Science-Technology\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"SUCH-TV\"], \"genres\": [\"Entertainment\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"SUCH-TV\"], \"genres\": [\"Health\"]}'"
    "curl --location 'https://gxkk3yzxg3rgaykek37gjccxgi0apfgr.lambda-url.eu-north-1.on.aws/ingest' --header 'Content-Type: application/json' --data '{\"sources\": [\"Ariana-News\"], \"genres\": [\"Top-News\"]}'"

    # ... (Include all your CURL commands here)
)

# Loop through each CURL command and execute with a 2-second delay
for command in "${curl_commands[@]}"; do
    echo -e "\n\n$command"
    eval "$command"  # Execute the command
done