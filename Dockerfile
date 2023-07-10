# syntax=docker/dockerfile:1


FROM python:3.8-slim-buster
WORKDIR /app
ENV OPENAI_KEY=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
ENV BRAVE_KEY=BSAv1neIuQOsxqOyy0sEe_ie2zD_n_V

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "app.py"]