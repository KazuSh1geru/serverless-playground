FROM public.ecr.aws/lambda/python:3.12

# yum: install devel & commands.
#RUN yum update -y && yum install -y gcc make ...

ARG lib_dir=./lambda_serverless
# pip: install python modules.
COPY Pipfile ./
COPY Pipfile.lock ./
RUN pip install pipenv && \
    pipenv requirements > requirements.txt && \
    pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy function code
COPY ${lib_dir}/*.py ${LAMBDA_TASK_ROOT}

# Compatible with initial base image
CMD ["app.lambda_handler"]
