# ---- Build-Stage: Astro statisch bauen ----
FROM node:20-alpine AS build
WORKDIR /app

# Nur Manifeste kopieren → Layer-Cache für Dependencies
COPY package.json package-lock.json ./
RUN npm ci

# Quellcode kopieren und statisch bauen (Ergebnis in /app/dist)
COPY . .
RUN npm run build

# ---- Runtime-Stage: nginx liefert dist/ auf Port 80 ----
FROM nginx:alpine AS runtime

# Eigene Server-Config (Directory-URLs, Caching, gzip)
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Statisches Build-Ergebnis in den nginx-Webroot
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
