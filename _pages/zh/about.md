---
layout: default
title: "关于"
permalink: /zh/about/
nav_exclude: true
lang: zh
lang_link: /about/
---

# 关于 HydroSense

HydroSense 是一套面向水文学、水资源与地球系统科学研究人员的自动化文献监测系统。

## 工作原理

### 双模式运作

**每日采集**通过 CrossRef 扫描 11 种顶级期刊，使用 Semantic Scholar 与 OpenAlex 补充摘要与领域信息，并应用确定性筛选条件（关键词、领域分类、同行评审状态）。Claude 大语言模型负责相关性判断与摘要生成。

**每周文献综述**通过关键词在 Semantic Scholar 与 OpenAlex 中进行检索（不限期刊），对结果去重后由 Claude 按主题方向进行综合分析。

### 数据来源

1. **CrossRef API** — 期刊级别论文元数据（每日采集）
2. **Semantic Scholar** — 领域分类、摘要与关键词检索
3. **OpenAlex** — 关键词检索与补充摘要
4. **Claude** — LLM 相关性评估与主题综合

### 论文登记表

一个中央登记表记录所有运行流程中出现过的 DOI。被多条路径发现（每日 + 每周，或多个检索主题）的论文会被标记为"重要论文"——这是相关性的强信号。

### 关注主题

- 水文学与水文建模
- 河流系统与径流
- 水库与水资源管理
- 洪水与干旱
- 气候变化对水的影响
- 陆面建模
- 季节性预测
- 水力发电与灌溉
- 地球系统模型

### 研究方向

本系统主要面向以下方向的研究人员：

- E3SM（能源外延性地球系统模型）
- MOSART 河道汇流模型
- 陆-河耦合与连通性
- 水库调度与管理
- 大尺度水文建模

## 监测期刊

### 顶级期刊（11 种）

- Nature
- Science
- Proceedings of the National Academy of Sciences (PNAS)
- Geophysical Research Letters (GRL)
- Bulletin of the American Meteorological Society (BAMS)
- Nature Climate Change
- Nature Geoscience
- Nature Water
- Reviews of Geophysics
- Nature Communications
- Nature Reviews Earth & Environment

### 高影响力专业期刊（18 种）

- Water Resources Research (WRR)
- Journal of Hydrology (JoH)
- Hydrology and Earth System Sciences (HESS)
- Advances in Water Resources (AWR)
- Journal of Climate
- Earth System Dynamics
- Global Change Biology
- Environmental Research Letters
- Journal of Geophysical Research: Atmospheres
- Journal of Hydrometeorology
- Journal of Advances in Modeling Earth Systems (JAMES)
- Earth-Science Reviews
- Journal of Geophysical Research: Machine Learning and Computation
- Geoscientific Model Development (GMD)
- Earth's Future
- Scientific Data
- Scientific Reports
- Hydrological Processes
- Journal of the American Water Resources Association (JAWRA)

## 技术栈

- **采集程序**: Python 3.7+ 与 requests 库
- **API**: CrossRef、Semantic Scholar、OpenAlex
- **LLM**: Claude（通过定时触发器调用）
- **网站**: Jekyll + Just the Docs 主题
- **搜索**: 全文检索（包括论文摘要）
- **托管**: GitHub Pages

## 参与贡献

这是一个开源项目。采集脚本与网站代码可在 [HydroSense GitHub 仓库](https://github.com/hydrotian/HydroSense)中查看。

## 联系方式

如有疑问或建议：
- 邮箱：hydro.luna.bot@gmail.com
- GitHub Issues: [HydroSense Issues](https://github.com/hydrotian/HydroSense/issues)

---

*最后更新：2026 年 3 月*
