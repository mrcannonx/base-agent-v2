# Environment Variables

## Required Variables

### Supabase Configuration
- `SUPABASE_URL`: Supabase project URL
- `SUPABASE_KEY`: Supabase anon/public key
- `SUPABASE_SERVICE_KEY`: Supabase service role key

### Database Configuration
- `DATABASE_URL`: PostgreSQL connection string
  Format: `postgresql://user:password@host:port/database`

### Application Configuration
- `PYTHON_VERSION`: Python version (e.g., 3.9)
- `SECRET_KEY`: Application secret key for encryption
- `DEBUG`: Set to `True` for development, `False` for production

## Optional Variables

### Email Configuration
- `EMAIL_HOST`: SMTP server host
- `EMAIL_PORT`: SMTP server port
- `EMAIL_USER`: SMTP username
- `EMAIL_PASSWORD`: SMTP password

### Cache Configuration
- `REDIS_URL`: Redis connection URL
