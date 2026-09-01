---
name: create-client
description: >-
  Generates a typed Python HTTP API client from a local OpenAPI/Swagger JSON (or YAML)
  document using openapi-python-client. Writes the client under a `generated/` directory
  next to the spec. Use when the user provides a path to swagger.json, openapi.json,
  OpenAPI YAML, or asks for a Python client from an API spec.
---

# Create Python API client from spec

## Tool

Use **[openapi-python-client](https://github.com/openapi-generators/openapi-python-client)** (PyPI: `openapi-python-client`). It targets **OpenAPI 3.0 / 3.1**, generates an **httpx** + **Pydantic** client, and supports **`--meta uv`** so the generated package matches this repo’s **uv** layout.

It does **not** support **OpenAPI 2.x (Swagger 2.0)** as-is. If the document has a top-level `"swagger": "2.0"`, convert it to OpenAPI 3 first (for example `npx -y swagger2openapi path/to/swagger.json -o path/to/openapi3.json`), then run generation on the converted file and still emit output under `generated/` as below.

## Install (this project)

From the repo root:

```bash
uv sync --group dev
```

If `uv` is unavailable, use any environment where dev dependencies are installed (for example `pip install -e ".[dev]"` if your packaging exposes dev extras).

Invoke the CLI as:

```bash
uv run python -m openapi_python_client generate ...
```

(or `python -m openapi_python_client generate ...` when the active environment already has `openapi-python-client` installed).

## Inputs and outputs

- **Input**: absolute or relative path to the API document (commonly `swagger.json`; may be `.yaml` / `.yml` if the tool is pointed at that path).
- **Output directory**: `<parent_directory_of_the_spec_file>/generated/`

Example: spec is `/Users/me/apis/acme/swagger.json` → client is written under `/Users/me/apis/acme/generated/`.

## Steps

1. Resolve the spec path to an absolute path for clarity. Let `SPEC_DIR` be the directory containing the spec file.
2. Ensure the output directory exists (the generator does not create missing parent paths):

   ```bash
   mkdir -p "${SPEC_DIR}/generated"
   ```

3. Generate the client (use `--overwrite` when replacing an existing client):

   ```bash
   uv run python -m openapi_python_client generate \
     --path "${SPEC_FILE}" \
     --output-path "${SPEC_DIR}/generated" \
     --meta uv \
     --overwrite
   ```

4. If generation fails with an OpenAPI 2.x / unsupported document error, convert the spec to OpenAPI 3, write a temporary OpenAPI 3 file next to the original (for example `${SPEC_DIR}/openapi3.json`), then rerun step 3 with `--path` pointing at that file. Keep the final layout under `${SPEC_DIR}/generated`.

5. If the api directory, or the models directory, and other files are in a subdirectory under `${SPEC_DIR}/generated`, please move all folders and files in that subfolder to `${SPEC_DIR}/generated`, and delete the subdirectory.

6. Optionally run `uv sync` inside `${SPEC_DIR}/generated` if the user wants dependencies installed immediately (the generator emits a small uv project there when `--meta uv` is used).

7. Tell the user where the client was written and that **ruff** post-hooks in the generator may require **ruff** on `PATH` (this repo already includes ruff in dev dependencies).

## Notes

- Prefer **`--meta uv`** for consistency with uv-based workflows.
- Treat `swagger.json` as a **filename convention**; the format must be OpenAPI 3 unless converted from Swagger 2.
- Do not commit secrets; generated clients may include default `base_url` values from the spec—review before sharing.
