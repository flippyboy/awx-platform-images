# Build the Ansible Platform UI from ansible-ui source and serve with nginx.
# Build context: repository root (this project).
#
# Upstream ansible-ui is copied unmodified; compose-specific fixes are applied
# as patches under docker/platform-ui/patches/ during this build.
#
#   docker build -f docker/platform-ui/Dockerfile -t awx-compose/platform-ui:local .

FROM node:22-bookworm AS builder

WORKDIR /src

# Install dependencies (workspace monorepo) — layer-cache friendly
COPY ansible-ui/package.json ansible-ui/package-lock.json ansible-ui/nx.json \
     ansible-ui/tsconfig.json ansible-ui/tsconfig.cjs.json ./
COPY ansible-ui/framework/package.json ./framework/
COPY ansible-ui/frontend/common/package.json ./frontend/common/
COPY ansible-ui/frontend/awx/package.json ./frontend/awx/
COPY ansible-ui/frontend/eda/package.json ./frontend/eda/
COPY ansible-ui/frontend/hub/package.json ./frontend/hub/
COPY ansible-ui/frontend/chatbot/package.json ./frontend/chatbot/
COPY ansible-ui/platform/package.json ./platform/
COPY ansible-ui/playwright/package.json ./playwright/

RUN npm ci --ignore-scripts

# Copy sources needed for the platform build (unmodified upstream tree)
COPY ansible-ui/framework ./framework
COPY ansible-ui/frontend ./frontend
COPY ansible-ui/platform ./platform
COPY ansible-ui/locales ./locales
COPY ansible-ui/webpack ./webpack
COPY ansible-ui/types ./types
COPY ansible-ui/babel.config.json ./

# Apply compose-only patches (keeps ansible-ui/ checkout clean for upgrades)
COPY docker/platform-ui/patches /patches
RUN set -eux; \
    if [ -d /patches ] && ls /patches/*.patch >/dev/null 2>&1; then \
      for p in /patches/*.patch; do \
        echo "Applying $p"; \
        patch -p1 < "$p"; \
      done; \
    fi

# Relative API prefixes so the browser hits the same origin (Jewel/Envoy).
ENV PLATFORM_SERVER=""
RUN cd platform && npm run build

# --- Runtime ---
FROM nginx:1.27-alpine AS runtime

COPY docker/platform-ui/nginx-default.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /src/platform/dist /usr/share/nginx/html

EXPOSE 8080
HEALTHCHECK --interval=10s --timeout=3s --retries=5 \
  CMD wget -qO- http://127.0.0.1:8080/ >/dev/null || exit 1

CMD ["nginx", "-g", "daemon off;"]
