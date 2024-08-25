
# Use the official PostgreSQL image as the base
FROM postgres

# Optional: Set environment variables with defaults (they can be overridden by the .env file)
ENV POSTGRES_USER=${POSTGRES_USER:-default_user}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD:-default_password}
ENV POSTGRES_DB=${POSTGRES_DB:-default_db}

# Optional: Copy an initialization script into the image
COPY init.sql /docker-entrypoint-initdb.d/

# Expose the PostgreSQL port
EXPOSE 5432

