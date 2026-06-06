# 📊 AI Load Testing Tools

AI负载测试工具，支持压力测试、性能测试、基准测试。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🏗️ 负载测试设计
- 🦗 Locust脚本生成
- 📈 k6脚本生成
- 📊 结果分析
- 💥 压力测试设计
- 📏 基准测试生成

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_load_testing_tools import create_tools

tools = create_tools()

# 负载测试设计
test = tools.design_load_test("API服务", ["正常负载", "高峰负载"])

# Locust脚本
locust = tools.generate_locust_script(endpoints, 1000)

# k6脚本
k6 = tools.generate_k6_script(endpoints, 500)

# 结果分析
analysis = tools.analyze_load_test_results(results)

# 压力测试
stress = tools.design_stress_test("API服务", "10000并发")

# 基准测试
benchmark = tools.generate_benchmark("数据库查询", ["QPS", "延迟"])
```

## 📁 项目结构

```
ai-load-testing-tools/
├── tools.py       # 负载测试工具核心
└── README.md
```

## 📄 许可证

MIT License
