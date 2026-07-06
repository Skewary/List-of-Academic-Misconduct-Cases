# geng-academic-fraud-detector 兼容层

本目录用于兼容 [`wooly99/geng-academic-fraud-detector`](https://github.com/wooly99/geng-academic-fraud-detector) 生成的「耿同学打假报告」。该工具的 README 描述其用途是用 AI 辅助检测论文中的数据造假、图片复用、统计异常等问题，并按「耿同学六式」输出结构化报告。

## 兼容目标

- 保留工具生成的原始 Markdown 报告路径。
- 抽取报告中的「论文信息」「综合评定」「详细发现」。
- 将每个「发现」转为本仓库可维护的证据页草稿。
- 记录导入元数据到 [`../../data/tool_reports.csv`](../../data/tool_reports.csv)。
- 不把 AI 工具输出直接当成最终实锤；导入后的证据页仍需人工回到论文图表、补充材料或原始数据截图核对。

## 推荐工作流

1. 使用外部工具生成报告，例如：

   ```bash
   # 示例，具体安装和运行方式以该工具仓库为准
   npx skills add https://github.com/wooly99/geng-academic-fraud-detector
   ```

2. 将生成的 Markdown 报告保存到本仓库，例如：

   ```text
   imports/geng-detector/<person-id>/<paper-id>/report.md
   ```

3. 运行导入脚本：

   ```bash
   python3 scripts/import_geng_detector_report.py \
     imports/geng-detector/<person-id>/<paper-id>/report.md \
     --person-id <person-id> \
     --paper-id <paper-id>
   ```

4. 人工检查生成的证据页草稿，补充论文截图、图号、表号、补充材料文件名和原始数据定位。

## 字段映射

| 外部报告字段 | 本仓库字段/位置 |
| --- | --- |
| `# 耿同学打假报告` | `data/tool_reports.csv.report_id` 的来源之一 |
| `## 论文信息` | 证据页的论文信息摘要 |
| `## 综合评定` | `data/tool_reports.csv.overall_verdict` |
| `### 发现 N` | 生成一个证据页草稿 |
| `位置` | 证据页「可跳转定位」 |
| `描述` / `证据` / `判断逻辑` | 证据页「摘要」与「待人工核对」 |
| `严重程度` | 证据页「可信度与限制」中的初始严重程度 |
