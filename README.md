# DevOpsHub – Message Queue + Visit Counter with Redis

Midterm project (Cloud Computing and DevOps Engineering). Two Flask web apps share one Redis database, all run with Docker Compose.

| Service | Role | Port |
|---|---|---|
| `redis` | Database (message list + visit counter), persisted in a volume | not exposed |
| `app1` | Message Collector: form, counts visits, pushes messages | 5001 |
| `app2` | Dashboard: shows message count and visit count | 5002 |

## Shared contract (both apps must follow it)

- Redis host comes from env `REDIS_HOST` (value in compose: `redis`, the service name), port `6379`.
- Redis key `visits` – integer counter (`INCR`).
- Redis key `messages` – list of strings (`RPUSH`, size read with `LLEN`).

## Layout

```
app1/                 Message Collector (code + Dockerfile)
app2/                 Dashboard (code + Dockerfile)
docker-compose.yml    all 3 services
report/               submission report + screenshots
```

Work is tracked in the GitHub Issues. One branch + one pull request per issue.
