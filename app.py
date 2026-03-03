import streamlit as st
from agent.react_agent import ReactAgent
import time

# 标题
st.title('智扫通机器人智能客服')
# 分隔符
st.divider()

# 初始化 Agent
if 'agent' not in st.session_state:
    st.session_state['agent'] = ReactAgent()
# 初始化消息列表
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# 显示历史消息
for message in st.session_state['messages']:
    st.chat_message(message['role']).write(message['content'])

# 用户输入
prompt = st.chat_input()

if prompt:
    # 显示用户输入
    st.chat_message('user').write(prompt)
    st.session_state['messages'].append({'role': 'user', 'content': prompt})

    # AI客服回复
    response_messages = []
    with st.spinner('智能客服思考中...'):
        res_stream = st.session_state['agent'].execute_stream(prompt)

        def capture(generator, cache_list):
            for chunk in generator:
                cache_list.append(chunk)
                # 一个字一个字地输出
                for char in chunk:
                    time.sleep(0.01)
                    yield char
        
        st.chat_message('assistant').write_stream(capture(res_stream, response_messages))
        st.session_state['messages'].append({'role': 'assistant', 'content': response_messages[-1]})
        # 刷新页面, 去掉冗余的思考过程
        st.rerun()