from mcp.server.fastmcp import FastMCP
import datetime
import pytz

# Create an MCP server
mcp = FastMCP("date_mcp")

# 工具1：将13位毫秒时间戳转为东八区日期
@mcp.tool()
def timestamp_to_china_date(millis_timestamp: int) -> str:
    """将13位毫秒时间戳转换为东八区日期时间（含毫秒）
    
    Args:
        millis_timestamp (int): 13位毫秒级时间戳，如 1746773348432
    
    Returns:
        str: 东八区时间字符串，格式为 YYYY-MM-DD HH:MM:SS.sss
    """
    # 将毫秒转为秒（保留小数位）
    seconds = millis_timestamp / 1000
    # 创建UTC时间对象
    utc_time = datetime.datetime.fromtimestamp(seconds, pytz.utc)
    # 转换为东八区时间
    china_time = utc_time.astimezone(pytz.timezone("Asia/Shanghai"))
    # 格式化为字符串（精确到毫秒）
    return china_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

# 工具2：将东八区日期转为13位毫秒时间戳
@mcp.tool()
def china_date_to_timestamp(date_str: str) -> int:
    """将东八区日期时间字符串转为13位毫秒时间戳
    
    Args:
        date_str (str): 东八区时间字符串，格式支持两种：
                        - YYYY-MM-DD HH:MM:SS
                        - YYYY-MM-DD HH:MM:SS.sss
    
    Returns:
        int: 13位毫秒时间戳，如 1746773348432
    """
    # 尝试解析带毫秒的格式
    try:
        naive_time = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
    except ValueError:
        # 解析不带毫秒的格式
        naive_time = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    # 附加东八区时区信息
    china_tz = pytz.timezone("Asia/Shanghai")
    aware_time = china_tz.localize(naive_time)
    # 转为UTC时间并计算时间戳
    return int(aware_time.astimezone(pytz.utc).timestamp() * 1000)

# 保留你原有的工具和资源
@mcp.tool()
def get_date() -> str:
    utc_now = datetime.datetime.now(pytz.utc)
    china_time = utc_now.astimezone(pytz.timezone('Asia/Shanghai'))
    return china_time.strftime('%Y-%m-%d')

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    return f"Hello, {name}!"