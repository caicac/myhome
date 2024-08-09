import streamlit as st
from PIL import Image
import base64

page = st.sidebar.radio("首页", ["兴趣推荐", "工具", "词典", "留言区", "关于"])

def bar_bg(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        [data-testid='stSidebar'] > div:first-child {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

def page_bg(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

# bar_bg('KoBeicetea.jpg')
# page_bg('KoBeicetea.jpg')


def page_1():
    '兴趣推荐'

    st.title("每日纪念")
    st.write(':red[牢大想你了]:cry::cry::cry::cry::cry:')
    st.image("KoBeicetea.jpg")
    with open('seeyouaginx3.mp4', 'rb') as f:
        mymp4 = f.read()
    st.video(mymp4, format='video/mp4', start_time=0)
    st.title("每日启动")
    col1, col2, col3 = st.columns([10, 15, 10])
    with col1:
        st.markdown(f"[![image](https://webstatic.mihoyo.com/bh3/upload/officialsites/201908/ys_1565764084_7084.png)](https://ys.mihoyo.com/)")
    with col2:
        st.markdown(f"[![image](https://webstatic.mihoyo.com/upload/event/2022/07/29/3a4f0e55bfbb4205346b84ba1a0ecad2_6530919755834738418.png)](https://sr.mihoyo.com/)")
    with col3:
        st.markdown(f"[![image](https://zzz.mihoyo.com/_nuxt/img/绝区零2.004eacc.jpg)](https://zzz.mihoyo.com/main/)")


def page_2():
    '''工具'''
    tab_photo, tab_music, tab_video = st.tabs(["图片工具", "音频工具", "视频工具"])
    with tab_photo:
        st.write(":sunglasses:图片换色小程序:sunglasses:")
        uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
        if uploaded_file:
            # 获取图片文件的名称、类型和大小
            file_name = uploaded_file.name
            file_type = uploaded_file.type
            file_size = uploaded_file.size
            img = Image.open(uploaded_file)
            tab1, tab2, tab3, tab4 = st.tabs(["原图", "改色1", "改色2", "改色3"])
            with tab1:
                st.image(img)
            with tab2:
                st.image(img_change(img, 0, 2, 1))
            with tab3:
                st.image(img_change(img, 1, 2, 0))
            with tab4:
                st.image(img_change(img, 1, 0, 2))
            img.save(file_name)
            with open(file_name, "rb") as file:
                btn = st.download_button(
                    label="下载图片",
                    data=file,
                    file_name=f"{file_name}_修改",
                    mime=f"image/png")
    with tab_music:
        st.write(":sunglasses:音频格式小程序:sunglasses:")
        uploaded_file = st.file_uploader("选择音乐文件",
                                         type=['mp3', 'wav', 'aac', 'flac', 'ogg', 'wma', 'm4a', 'alac', 'aiff', 'ape',
                                               'opus', 'amr', 'pcm', 'ra', 'caf', 'ac3', 'dts', 'mka', 'aif', 'au',
                                               'snd', 'mid', 'midi'])
        if uploaded_file is not None:

            st.write("上传曲目: ", uploaded_file.name)
            formats = ['mp3', 'wav', 'aac', 'flac', 'ogg', 'wma', 'm4a', 'alac', 'aiff', 'ape', 'opus', 'amr', 'pcm',
                       'ra', 'caf', 'ac3', 'dts', 'mka', 'aif', 'au', 'snd', 'mid', 'midi']
            target_format = st.selectbox("需要转换格式", formats)

            if st.button("开始", key="1"):
                try:
                    st.download_button(
                        label=f"下载 {target_format.upper()} 文件",
                        data=uploaded_file,
                        file_name=f"{uploaded_file.name.split('.')[0]}.{target_format}",
                        mime=f"audio/{target_format}")
                except Exception as e:
                    st.warning("该音频文件似乎不支持这样转换，请尝试选择其他格式进行转换或更换音频文件")
    with tab_video:
        st.write(":sunglasses:视频格式小程序:sunglasses:")
        uploaded_file = st.file_uploader("选择视频文件",
                                         type=['mp4', 'avi', 'mkv', 'mov', 'wmv', 'flv', 'webm', 'm4v', 'mpeg', 'mpg',
                                               '3gp', 'ogg', 'ogv', 'vob', 'm2ts', 'mts', 'mxf', 'rm', 'rmvb', 'divx',
                                               'ts', 'm2v', 'f4v', 'asf', 'dv'])
        if uploaded_file is not None:

            st.write("上传视频: ", uploaded_file.name)
            formats = ['mp4', 'avi', 'mkv', 'mov', 'wmv', 'flv', 'webm', 'm4v', 'mpeg', 'mpg', '3gp', 'ogg', 'ogv',
                       'vob', 'm2ts', 'mts', 'mxf', 'rm', 'rmvb', 'divx', 'ts', 'm2v', 'f4v', 'asf', 'dv']
            target_format = st.selectbox("需要转换格式", formats)

            if st.button("开始", key="2"):
                try:
                    st.download_button(
                        label=f"下载 {target_format.upper()} 文件",
                        data=uploaded_file,
                        file_name=f"{uploaded_file.name.split('.')[0]}.{target_format}",
                        mime=f"audio/{target_format}")
                except Exception as e:
                    st.warning("该视频文件似乎不支持这样转换，请尝试选择其他格式进行转换或更换视频文件")

    #     st.audio(uploaded_file, format='audio/mp3', start_time=0)
    # uploaded_file = st.file_uploader("选择视频文件")
    # if uploaded_file is not None:
    #     st.write("视频名:", uploaded_file.name)
    #     st.video(uploaded_file, start_time=0)


def page_3():
    '词典'
    st.write("智能词典")
    with open("words_space.txt", 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split("#")
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
        
    with open("check_out_times.txt", 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split("#")
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
        
    word = st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w',encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)

        st.write('查询次数:', times_dict[n])
        if word == "man":
            st.code('''
                    what can I say
                    ''')
            st.balloons()
            # st.snow()


def page_4():
    '留言区'
    st.write('留言区')
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split("#")
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🍉'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🍅'):
                st.write(i[1],':',i[2])
        elif i[1] == '游客':
            with st.chat_message('🍂'):
                st.text(i[1]+':'+i[2])
    name = st.selectbox('我是......',['阿短','编程猫','游客'])
    new_message = st.text_input('想要说的话......')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

def page_5():
    '关于'
    st.title('关于')
    st.write('----')
    st.write('除了本主站之外，我还将我的有趣内容分享在了其他网站中')
    st.markdown('**你的支持是我最大的动力，去支持一下up吧！目前建设中，现在关注我，你就是我老粉了qwq**')
    url = "https://space.bilibili.com/17658938"
    image_url = "https://i0.hdslb.com/bfs/archive/c8fd97a40bf79f03e7b76cbc87236f612caef7b2.png"
    st.markdown(f"[![image]({image_url})]({url})")


def img_change(img, rc, gc, bc):
    '图片处理'
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img


if (page == '兴趣推荐'):
    page_1()
elif (page == '工具'):
    page_2()
elif (page == '词典'):
    page_3()
elif (page == '留言区'):
    page_4()
elif (page == '关于'):
    page_5()
else:
    pass
