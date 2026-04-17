import json

# --- 配置区 ---
INCLUDE_THOUGHTS = False
INPUT_JSON_FILE = '形式幂级数拉格朗日反演入门.json'  # 输入JSON文件名(将下载的对话修改为这个名字，放在代码同一目录下)
OUTPUT_TEXT_FILE = 'conversation.txt' # 输出文本文件名

# --- 核心逻辑 ---
try:
    # 读取并解析JSON文件
    with open(INPUT_JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 提取对话内容块
    chunks = data.get('chunkedPrompt', {}).get('chunks', [])
    
    output_content = ""

    for chunk in chunks:
        # 跳过非字典或无文本的块
        if not isinstance(chunk, dict) or 'text' not in chunk:
            continue

        text = chunk['text'].strip()
        
        # 处理思考过程
        if chunk.get('isThought'):
            if INCLUDE_THOUGHTS:
                output_content += f"{'='*25} 🧠 模型思考中... {'='*25}\n{text}\n{'='*70}\n\n"
            continue

        # 处理用户和模型的对话
        role = chunk.get('role')
        if role == 'user':
            output_content += f"👤 用户:\n{text}\n\n{'-'*50}\n\n"
        elif role == 'model':
            output_content += f"🤖 模型:\n{text}\n\n{'-'*50}\n\n"
            
    # 将结果写入文件
    with open(OUTPUT_TEXT_FILE, 'w', encoding='utf-8') as f:
        f.write(output_content)

    print(f"✅ 处理完成！对话内容已保存到: {OUTPUT_TEXT_FILE}")

except FileNotFoundError:
    print(f"❌ 错误：找不到文件 '{INPUT_JSON_FILE}'。")
except Exception as e:
    print(f"❌ 处理过程中发生错误: {e}")