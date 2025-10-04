# ----- Stage 1 : Build ------
FROM python:3.11-slim AS build

WORKDIR /app

# Installing requirements
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/app/modules -r requirements.txt

# Bytecode compiled
COPY src ./src
RUN python -m compileall -b src \
    && mv src __app__ \
    && python -m zipapp __app__ -o app.pyz


# ----- Stage 2 : Run -----
FROM python:3.11-slim AS run

# Create user
RUN groupadd -r app && useradd -r -g app app

WORKDIR /app

COPY --from=build /app/modules /usr/local
COPY --from=build /app/app.pyz .

RUN chown -R app:app /app
USER app

ENTRYPOINT ["python", "app.pyz"]
