# 从server模块导入mcp实例
from servers.server import mcp


def main():
    """主函数，启动MCP服务器"""
    print("Starting MCP Demo Server...")
    # 这里可以添加其他初始化代码


if __name__ == "__main__":
    main()
    # 使用stdio传输方式启动服务器
    mcp.run(transport='stdio')