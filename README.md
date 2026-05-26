# AI 安全工具集
这是一组用于 AI 安全工具匹配、参数检查和报告生成的 Python 脚本。

## 文件说明
- `choose_openclaw.py`：安全工具匹配类
- `tool_parameter_check.py`：AI 保护工具评估函数
- `AI_tool_report.py`：数据分析与报告生成功能

## 使用方法
使用python语言环境及编译器

## choosing.py
这边第一个代码choosing.py目的是帮助用户找到合适的防护工具，通过5个问题，从已有的几个防护工具中做出一个推荐。
## parameter-calc.py
如果没有找到满意的或者想增加备选防护工具，可以使用第二个parameter-calc.py来对于你的防护工具进行各方面参数的计算。注意这里我选用的防护工具是promptfoo，所以代码格式用户可以自行调整，运行的条件是防护工具.yaml和代码在一个文件夹内。若防护工具不是.yaml形式，可自行改代码。
## report.py
第三个代码report.py是根据你的防护工具，生成一个网页版的报告，直观简洁，可以辅助用户进行防护工具的选择。         上
