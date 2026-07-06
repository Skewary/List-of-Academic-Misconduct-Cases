# 学术造假论文证据库

本仓库用于用民间力量长期整理 **Bilibili 博主「耿同学讲故事」** 已公开点名或重点讲解过的科研人员、论文和论文内部证据。

项目目标不是等待学校、期刊或司法机关通报，而是把论文里的可复核证据整理成可跳转、可截图、可追踪的资料库：谁、哪篇论文、哪张图、哪组数据、异常在哪里。

## 目录导航

- [`people/`](people/)：人物条目，每位人物一个独立目录。
- [`cases/`](cases/)：按事件、学校、研究领域或异常类型整理的案例页。
- [`evidence/`](evidence/)：跨人物证据索引，重点记录论文图、补充数据、视频时间戳。
- [`papers/`](papers/)：论文条目与元数据。
- [`screenshots/`](screenshots/)：论文原文、补充材料、视频讲解中的关键截图。
- [`data/`](data/)：结构化表格数据，便于后续生成网页或统计。
- [`templates/`](templates/)：新增人物、论文、证据、截图时使用的模板。
- [`site/`](site/)：静态 HTML 入口页，便于直观浏览。
- [`docs/`](docs/)：维护规范、证据标准、命名规范。

## 已搜集的初始名单

初始名单来自对「耿同学讲故事」相关公开视频标题、媒体报道和网页检索结果的整理。每个条目后续都应回到论文正文、图版和补充材料中补齐截图与定位。

| 人物 | 机构/身份线索 | 耿同学相关视频或线索 | 论文内证据重点 | 本地条目 |
| --- | --- | --- | --- | --- |
| 王平 | 同济大学生命科学与技术学院时任院长 | [同济大学，百万经费的nature论文，数据造假过于明显](https://www.bilibili.com/video/BV1NEDnBbEkA/) | 固定差值、末位数字集中、列间规律性加减等数据异常 | [`people/wang-ping/`](people/wang-ping/) |
| 陈佺 | 南开大学生命科学学院院长 | [南开生科院长，nature子刊，离谱造假](https://www.bilibili.com/video/BV1oWo9BRE25/) | 补充材料中多组数据小数点后两位一致、数据重复、末位分布异常 | [`people/chen-quan/`](people/chen-quan/) |
| 康铁邦 | 中山大学肿瘤防治中心实验研究部副主任 | [中山大学，国家科技进步二等奖得主，Nature子刊，离谱造假](https://www.bilibili.com/video/BV1XyRiB8ErL/) | 论文图片/数据异常，待回到原论文逐图标注 | [`people/kang-tiebang/`](people/kang-tiebang/) |
| 邝栋明 | 中山大学生命科学学院副院长 | 视频合集线索：又是中山大学，生科院副院长代表作，造假 | 论文图片/数据异常，待补充具体图号 | [`people/kuang-dongming/`](people/kuang-dongming/) |
| 苏佳灿 | 上海大学转化医学研究院院长 | [上海大学院长，代表作论文，严重造假](https://www.bilibili.com/video/BV1o65A6kEYH/) | 代表作论文图片/数据异常，待补充具体图号 | [`people/su-jiacan/`](people/su-jiacan/) |
| 常凌乾 | 北京航空航天大学医学科学与工程学院副院长 | 网页检索线索显示耿同学曾质疑相关 Nature 论文 | 实验数据过度规律/完美，待补充视频与论文链接 | [`people/chang-lingqian/`](people/chang-lingqian/) |

结构化版本见 [`data/seed_cases.csv`](data/seed_cases.csv)。

## 快速开始：新增一位人物

1. 复制 [`templates/person.md`](templates/person.md) 到 `people/<slug>/index.md`。
2. 复制 [`templates/paper.md`](templates/paper.md) 到 `people/<slug>/papers/<paper-slug>.md` 或 `papers/<paper-slug>.md`。
3. 复制 [`templates/evidence.md`](templates/evidence.md) 到 `people/<slug>/evidence/<evidence-id>.md`。
4. 将论文原图、补充材料表格、视频讲解关键帧放入 `screenshots/<slug>/`，并为每张截图建立说明文件。
5. 更新 [`data/people.csv`](data/people.csv)、[`data/papers.csv`](data/papers.csv)、[`data/evidence.csv`](data/evidence.csv) 或 [`data/seed_cases.csv`](data/seed_cases.csv)。
6. 在人物页中使用相对链接连接论文、证据、截图和表格数据。

## 证据原则

- 证据优先级：论文正文图表、补充材料、原始数据文件、论文页面、耿同学视频时间戳。
- 不要求学校通报、期刊声明、法院/行政文件；这些只能作为背景，不作为本项目的必需证据。
- 每条关键判断必须定位到「论文中的哪张图、哪张表、哪一列数据或哪一个补充文件」。
- 截图必须记录来源 URL、截图时间、论文图号/表号、视频时间戳或页面位置。
- 未回到论文原文核对的内容必须标注为「待核实」。

## 当前状态

项目已提供长期维护所需的目录结构、模板、数据表头和一份待补全的初始名单；人物页目前以占位目录为主，下一步应逐个补齐论文截图和证据定位。
