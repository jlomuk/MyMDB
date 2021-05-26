FROM python

ENV PATH="/scripts:${PATH}"

RUN mkdir /mymdb
WORKDIR /mymdb
COPY ./requirements* /mymdb/
COPY django/ /mymdb/django
COPY scripts/ /mymdb/scripts
RUN chmod +x /mymdb/scripts/entrypoint.sh

RUN apt-get -y update
RUN pip install -r requirements.prod.txt


CMD ["/mymdb/scripts/entrypoint.sh"]


EXPOSE 80
