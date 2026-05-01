import os
import subprocess
import sys
import shutil
from pathlib import Path

# 定义路径
results_dir = Path("reports/allure-results")
report_dir = Path("reports/allure-report")

# 删除旧结果目录
if results_dir.exists():
    shutil.rmtree(results_dir)

# 运行 pytest，如果失败则退出
pytest_result = subprocess.run([sys.executable, "-m", "pytest"])
if pytest_result.returncode != 0:
    print("pytest 执行失败，停止生成报告")
    sys.exit(pytest_result.returncode)

# 生成 Allure 报告
allure_result = subprocess.run(
    ["allure", "generate", str(results_dir), "-o", str(report_dir), "--clean"]
)
if allure_result.returncode != 0:
    print("Allure 报告生成失败")
    sys.exit(allure_result.returncode)

print("报告生成完成")