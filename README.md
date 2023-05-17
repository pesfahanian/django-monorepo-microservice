# Django Monorepo Microservice

Simple payment application utilizing [Monorepo](https://monorepo.tools/) codebase architecture and [Microservice](https://microservices.io/) deployment architecture.

The Monorepo codebase architecture was achieved **without** using any of the traditional build tools (_e.g._ [Bazel](https://bazel.build/), [Pants](https://www.pantsbuild.org/)).

---

## Services

### Wallet:

-   Simple CRUD operations
-   Deposit and withdraw features
-   Functionalities:
    -   Database
    -   REST API
    -   Admin panel
    -   Async events
    -   gRPC communication

### Ledger:

-   Double-entry ledger
-   Simple transaction journal
-   Functionalities:
    -   Database
    -   Admin panel
    -   Async events

### PG:

-   Bank API proxy middleman.
-   Functionalities:
    -   Ephemeral
    -   gRPC communication

---
