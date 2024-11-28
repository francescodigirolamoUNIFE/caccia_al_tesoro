FROM python

WORKDIR home/caccia_al_tesoro

COPY dist/caccia_al_tesoro-0.0.1-py3-none-any.whl .

RUN ["python","-m","pip","install","caccia_al_tesoro-0.0.1-py3-none-any.whl"]
