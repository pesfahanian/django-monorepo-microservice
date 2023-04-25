# Django Monorepo Microservice

### Services:

-   Service 1
    -   Database
    -   REST API
    -   Async events
    -   gRPC communication
-   Service 2
    -   Database
    -   Async events
-   Service 3
    -   Ephemeral
    -   gRPC communication

---

## Usage

Install all the requirements:

```sh
./scripts/install.sh --all
```

> To install the development requirements, use the `--develop` or `-D` flag.

> To install the requirements of only one service, run `./scripts/install.sh <SERVICE NAME>`.

Generate JWT RS256 key-pair:

```sh
./scripts/keygen.sh
```

Generate gRPC codes:

```sh
./scripts/codegen.sh
```
