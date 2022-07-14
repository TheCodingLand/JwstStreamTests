
# Intro

Analysis of 
https://webbtelescope.org/contents/media/images/2022/031/01G77PKB8NKR7S8Z6HBXMYATGJ


## Setup:

`docker-compose up -d`

Then attach Vscode to container jswt_dev_env

## Only download data:

`docker-compose up -d jwstdata_downloader`


## Start jupyter:

From inside vscode in the dev container:
`jupyter notebook`

## Start jdaviz:

`jdaviz cubeviz /workspace/volumes/jwst_data/jw02731/jw02731001001/jw02731001001_02101_00004_nrcb3_rate.fits`


