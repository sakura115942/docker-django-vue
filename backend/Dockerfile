FROM python:3.9-slim-buster

ENV environment production

COPY ./ /app
WORKDIR /app
RUN bash -c 'echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye main contrib non-free" > /etc/apt/sources.list'

RUN apt-get update && \
	apt-get install -y libpq-dev gcc

RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r /app/requirements.txt && \
    pip install gunicorn

ENTRYPOINT /app/entrypoint.sh
