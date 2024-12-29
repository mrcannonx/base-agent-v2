# Deployment Guide

## Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/mrcannonx/base-agent.git
   cd base-agent
   ```

2. Install dependencies:
   ```bash
   npm install && poetry install
   ```

3. Set up environment variables (see env-vars.md)

4. Start development servers:
   ```bash
   npm run dev:all
   ```

## Production Deployment

### Vercel Deployment

1. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Deploy to Vercel:
   ```bash
   vercel
   ```

3. Set environment variables in Vercel dashboard

### Build Process

1. Create production build:
   ```bash
   npm run build
   ```

2. The build process will:
   - Compile frontend assets
   - Package Python backend
   - Generate optimized production artifacts

### Configuration

- `vercel.json`: Vercel configuration file
- `.vercelignore`: Files to exclude from deployment

## Monitoring

- Check deployment logs:
  ```bash
  vercel logs
  ```

- View deployment status:
  ```bash
  vercel list
