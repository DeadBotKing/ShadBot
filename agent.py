import json

available_tools = {
    'list_workspace': {'purpose': 'List the actual files and directories inside the workspace.', 'arguments': {}}
}

def execute(tool_name, arguments):
    if tool_name not in available_tools:
        return {'error': 'Tool not found'}
    try:
        result = globals()[tool_name](**arguments)
        return json.dumps(result)
    except Exception as e:
        return {'error': str(e)}

def main():
    while True:
        user_input = input('Qwen: ')
        command, *args = user_input.split()
        args = [json.loads(arg) for arg in args]
        result = execute(command, args[0])
        print(result)

if __name__ == '__main__':
    main()