FROM public.ecr.aws/lambda/python:3.6

MAINTAINER "ataj125@gmail.com"

COPY . ${LAMBDA_TASK_ROOT}
COPY requirements.txt ${LAMBDA_TASK_ROOT}

RUN pip install --upgrade pip
RUN pip install -r requirements.txt && pip install pymongo[srv]

# RUN mkdir bin
ADD bin /bin/

RUN chmod 755 /bin/chromedriver

CMD [ "main.handler" ]