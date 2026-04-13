#!/bin/sh
set -eu

if find /usr/local/share/ca-certificates -type f -name '*.crt' | grep -q .; then
  update-ca-certificates
fi

bundle config set path '/usr/local/bundle'

if [ "$#" -eq 0 ]; then
  set -- bundle exec jekyll serve \
    --host 0.0.0.0 \
    --port 4000 \
    --livereload \
    --livereload-port 35729 \
    --force_polling
fi

case "${1:-}" in
  bundle)
    if [ "${2:-}" != "install" ] && ! bundle check; then
      bundle install
    fi
    ;;
  jekyll)
    if ! bundle check; then
      bundle install
    fi
    set -- bundle exec "$@"
    ;;
  *)
    if ! bundle check; then
      bundle install
    fi
    ;;
esac

exec "$@"
