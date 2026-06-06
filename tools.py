"""
AI Load Testing Tools - AI负载测试工具
支持压力测试、性能测试、基准测试
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AILoadTestingTools:
    """
    AI负载测试工具
    支持：压力、性能、基准
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def design_load_test(self, application: str, scenarios: List[str]) -> Dict:
        """设计负载测试"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        scenarios_text = ", ".join(scenarios)

        prompt = f"""请为{application}设计负载测试：

场景：{scenarios_text}

请返回JSON格式：
{{
    "test_plan": "测试计划",
    "scenarios": [
        {{"name": "场景", "users": "用户数", "duration": "时长"}}
    ],
    "metrics": ["监控指标"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"load_test": content}

    def generate_locust_script(self, endpoints: List[Dict], users: int) -> str:
        """生成Locust脚本"""
        if not self.client:
            return "LLM客户端未配置"

        endpoints_text = json.dumps(endpoints, ensure_ascii=False)

        prompt = f"""请生成Locust负载测试脚本：

端点：{endpoints_text}
并发用户：{users}

要求：
1. 完整的Locust类
2. 权重分配
3. 思考时间"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_k6_script(self, endpoints: List[Dict], vus: int) -> str:
        """生成k6脚本"""
        if not self.client:
            return "LLM客户端未配置"

        endpoints_text = json.dumps(endpoints, ensure_ascii=False)

        prompt = f"""请生成k6负载测试脚本：

端点：{endpoints_text}
虚拟用户：{vus}

要求：
1. 完整的k6脚本
2. 场景配置
3. 阈值设置"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def analyze_load_test_results(self, results: Dict) -> Dict:
        """分析负载测试结果"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        results_text = json.dumps(results, ensure_ascii=False)

        prompt = f"""请分析负载测试结果：

{results_text}

请返回JSON格式：
{{
    "summary": "总结",
    "bottlenecks": ["瓶颈"],
    "recommendations": ["建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"analysis": content}

    def design_stress_test(self, application: str, breaking_point: str) -> Dict:
        """设计压力测试"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{application}设计压力测试：

预期断点：{breaking_point}

请返回JSON格式：
{{
    "phases": [
        {{"phase": "阶段", "users": "用户数", "duration": "时长"}}
    ],
    "monitoring": ["监控指标"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"stress_test": content}

    def generate_benchmark(self, component: str, metrics: List[str]) -> str:
        """生成基准测试"""
        if not self.client:
            return "LLM客户端未配置"

        metrics_text = ", ".join(metrics)

        prompt = f"""请为{component}生成基准测试：

指标：{metrics_text}

要求：
1. Python代码
2. 多次运行
3. 统计分析"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content


def create_tools(**kwargs) -> AILoadTestingTools:
    """创建负载测试工具"""
    return AILoadTestingTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Load Testing Tools")
    print()

    # 测试
    test = tools.design_load_test("API服务", ["正常负载", "高峰负载"])
    print(json.dumps(test, ensure_ascii=False, indent=2))
