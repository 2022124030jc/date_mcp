# Date-MCP 服务

一个基于Model Context Protocol (MCP)的日期时间处理服务，专注于处理东八区（中国）时间与时间戳的转换。

## 功能特点

- **获取当前日期**：返回东八区（中国）当前日期
- **时间戳转换**：将13位毫秒级时间戳转换为东八区日期时间
- **日期转时间戳**：将东八区日期时间字符串转换为13位毫秒级时间戳
- **问候资源**：提供简单的问候功能

## 系统要求

- Python >= 3.13
- 依赖包：mcp[cli] >= 1.9.1, pytz

## 安装说明

1. 克隆仓库

```bash
git clone <仓库地址>
cd date_mcp
```

2. 安装依赖

```bash
pip install -e .
```

或使用 uv 安装（推荐）：

```bash
uv pip install -e .
```

## 使用方法

### 启动服务

```bash
python main.py
```

或使用 MCP CLI 工具：

```bash
mcp dev main.py
```

### 可用工具

1. **获取当前日期**

```python
# 工具名: get_date
# 返回格式: YYYY-MM-DD
response = await client.call_tool("get_date")
# 示例输出: "2024-05-28"
```

2. **时间戳转日期时间**

```python
# 工具名: timestamp_to_china_date
# 参数: millis_timestamp (int) - 13位毫秒级时间戳
response = await client.call_tool("timestamp_to_china_date", {"millis_timestamp": 1746773348432})
# 示例输出: "2025-05-09 12:35:48.432"
```

3. **日期时间转时间戳**

```python
# 工具名: china_date_to_timestamp
# 参数: date_str (str) - 东八区时间字符串
response = await client.call_tool("china_date_to_timestamp", {"date_str": "2025-05-09 12:35:48.432"})
# 示例输出: 1746773348432
```

### 可用资源

**问候资源**

```python
# 资源URI: greeting://{name}
# 参数: name (str) - 要问候的名称
response = await client.get_resource(f"greeting://World")
# 示例输出: "Hello, World!"
```

## 客户端示例

```python
from mcp.client import Client
from mcp.transport import StdioClientTransport

async def main():
    # 创建客户端
    transport = StdioClientTransport("python main.py")
    client = Client(transport)
    
    # 连接到服务器
    await client.connect()
    
    # 调用工具示例
    current_date = await client.call_tool("get_date")
    print(f"当前日期: {current_date}")
    
    # 时间戳转日期
    timestamp = 1746773348432
    date_time = await client.call_tool("timestamp_to_china_date", {"millis_timestamp": timestamp})
    print(f"时间戳 {timestamp} 对应的日期时间: {date_time}")
    
    # 日期转时间戳
    date_str = "2025-05-09 12:35:48.432"
    new_timestamp = await client.call_tool("china_date_to_timestamp", {"date_str": date_str})
    print(f"日期时间 {date_str} 对应的时间戳: {new_timestamp}")
    
    # 获取问候资源
    greeting = await client.get_resource("greeting://World")
    print(greeting)
    
    # 断开连接
    await client.disconnect()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

## 许可证



## 贡献指南

欢迎提交问题和拉取请求，共同改进这个项目。
        