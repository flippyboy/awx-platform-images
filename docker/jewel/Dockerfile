# Extend the public Jewel API image with the Platform UI.
#
#   docker build -f docker/jewel/Dockerfile \
#     --build-arg UI_IMAGE=awx-compose/platform-ui:local \
#     -t awx-compose/jewel:local .

ARG JEWEL_BASE=ghcr.io/ansible/jewel:latest
ARG UI_IMAGE=awx-compose/platform-ui:local

FROM ${UI_IMAGE} AS ui
FROM ${JEWEL_BASE} AS jewel-with-ui

USER root

RUN rm -rf /opt/aap_gateway/platform_ui/*
COPY --from=ui /usr/share/nginx/html/ /opt/aap_gateway/platform_ui/
RUN chown -R 1000:0 /opt/aap_gateway/platform_ui \
 && chmod -R g+rwX /opt/aap_gateway/platform_ui

# openssl for optional cert generation in entrypoint
RUN dnf install -y openssl 2>/dev/null || microdnf install -y openssl 2>/dev/null || true

USER 1000

LABEL org.opencontainers.image.title="Jewel with Platform UI" \
      org.opencontainers.image.description="Ansible Jewel gateway + ansible-ui platform UI"
