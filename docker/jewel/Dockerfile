# Extend the Jewel API image with the Platform UI.
#
# JEWEL_BASE is the image built from ansible/jewel at the pinned commit
# (scripts/prepare-jewel-context.sh, components.jewel.build: true), or the
# public ghcr.io/ansible/jewel image at its pinned digest.
#
#   docker build -f docker/jewel/Dockerfile \
#     --build-arg JEWEL_BASE=awx-compose/jewel-base:local \
#     --build-arg UI_IMAGE=awx-compose/platform-ui:local \
#     -t awx-compose/jewel:local .

ARG JEWEL_BASE=ghcr.io/ansible/jewel:latest
ARG UI_IMAGE=awx-compose/platform-ui:local

FROM ${UI_IMAGE} AS ui
FROM ${JEWEL_BASE} AS jewel-with-ui

USER root

# OS security updates, plus openssl for optional cert generation in the entrypoint.
RUN dnf -y upgrade --refresh \
 && dnf -y install openssl \
 && dnf clean all \
 && rm -rf /var/cache/dnf

# Python packages upstream still pins at vulnerable versions.
COPY docker/jewel/requirements-security.txt /tmp/requirements-security.txt
RUN /opt/aap_gateway/venv/bin/pip install --no-cache-dir --disable-pip-version-check \
      --no-deps -r /tmp/requirements-security.txt \
 && /opt/aap_gateway/venv/bin/pip check \
 && rm /tmp/requirements-security.txt

RUN rm -rf /opt/aap_gateway/platform_ui/*
COPY --from=ui /usr/share/nginx/html/ /opt/aap_gateway/platform_ui/
RUN chown -R 1000:0 /opt/aap_gateway/platform_ui \
 && chmod -R g+rwX /opt/aap_gateway/platform_ui

USER 1000

LABEL org.opencontainers.image.title="Jewel with Platform UI" \
      org.opencontainers.image.description="Ansible Jewel gateway + ansible-ui platform UI"
