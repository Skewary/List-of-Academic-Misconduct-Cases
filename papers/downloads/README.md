# 论文正文与补充材料下载区

本目录用于保存已有人物相关论文正文、补充材料、原始数据或下载日志。

当前执行过一次自动下载尝试，结果见 [`download-log.md`](download-log.md)，结构化清单见 [`../../data/download_attempts.csv`](../../data/download_attempts.csv)。由于当前 shell 网络访问多个出版商/数据库 URL 时遇到代理 `CONNECT tunnel failed: 403 Forbidden`，本次未能直接写入论文 PDF 或补充材料文件。

后续维护建议：

1. 在可访问出版商网页的网络环境中运行 `python3 scripts/download_known_papers.py`。
2. 若手动下载 PDF、补充材料或 Source Data，请放入对应人物目录，例如 `papers/downloads/wang-ping/`。
3. 下载后更新 `data/download_attempts.csv` 的 `status`、`local_path` 和 `notes`。
