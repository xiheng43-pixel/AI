class ClawSecurityMatch:
    def __init__(self):
        # 2026 主流防护工具数据库
        self.tools = {
            "腾讯龙虾管家": {"def": 85, "perf": 78, "ease": 98, "priv": 80, "desc": "国内小白首选，一键式防护，支持微信/手机提醒。"},
            "百度龙虾卫士": {"def": 82, "perf": 80, "ease": 95, "priv": 78, "desc": "百度安全生态，擅长拦截恶意插件，与浏览器深度集成。"},
            "ClawSecure": {"def": 92, "perf": 92, "ease": 85, "priv": 65, "desc": "Google云端防御，性能极佳，但高隐私需求下可能不适用。"},
            "NemoClaw": {"def": 96, "perf": 88, "ease": 60, "priv": 90, "desc": "英伟达硬件隔离，安全性极高，适合带GPU的高配环境。"},
            "ZeroClaw": {"def": 90, "perf": 65, "ease": 40, "priv": 98, "desc": "极致隐私，完全离线运行，适合军事/金融级敏感任务。"},
            "OpenFang": {"def": 75, "perf": 98, "ease": 55, "priv": 85, "desc": "Rust编写，几乎零延迟，适合追求高性能的开发者。"}
        }

    def run_quiz(self):
        print("="*50)
        print("   2026 OpenClaw 安全防护专家系统 (带一票否决)")
        print("="*50)
        
        # 1. 收集需求
        ans = {}
        ans['tech'] = input("\n1. 你的技术水平?\n(A.小白 B.懂配置 C.代码大佬): ").upper()
        ans['hw'] = input("\n2. 设备性能?\n(A.一般 B.还不错 C.顶级配置): ").upper()
        ans['scene'] = input("\n3. 主要用途?\n(A.日常娱乐 B.办公自动化 C.高机密处理): ").upper()
        ans['cloud'] = input("\n4. 隐私底线?\n(A.可接受云端 B.尽量本地 C.绝不能联网): ").upper()
        ans['speed'] = input("\n5. 响应要求?\n(A.安全第一,慢点行 B.均衡 C.必须秒回): ").upper()

        # 2. 初始化权重
        w = {"def": 0.2, "perf": 0.2, "ease": 0.2, "priv": 0.2}

        # 3. 动态调整权重 (Soft Logic)
        if ans['tech'] == 'A': w['ease'] += 0.5
        if ans['scene'] == 'C': w['def'] += 0.5
        if ans['speed'] == 'C': w['perf'] += 0.4
        if ans['cloud'] == 'C': w['priv'] += 0.6

        # 4. 执行“一票否决”机制 (Hard Constraints)
        filtered_tools = {}
        for name, m in self.tools.items():
            # 规则1: 如果选了最高机密(C)，防御力低于90的直接淘汰
            if ans['scene'] == 'C' and m['def'] < 90:
                continue
            # 规则2: 如果选了绝对不能联网(C)，隐私分低于90的直接淘汰
            if ans['cloud'] == 'C' and m['priv'] < 90:
                continue
            # 规则3: 如果是小白用户(A)，易用性低于70的直接淘汰（太难用你装不上）
            if ans['tech'] == 'A' and m['ease'] < 70:
                continue
            
            filtered_tools[name] = m

        # 5. 计算得分
        results = []
        for name, m in filtered_tools.items():
            score = (m['def'] * w['def'] + m['perf'] * w['perf'] + 
                     m['ease'] * w['ease'] + m['priv'] * w['priv'])
            results.append({"name": name, "score": round(score, 2), "desc": m['desc']})

        # 6. 输出匹配结果
        results.sort(key=lambda x: x['score'], reverse=True)

        if not results:
            print("\n[警告]：根据您的极端要求，目前市面上没有完美匹配的防护工具。建议降低部分维度需求。")
        else:
            top = results[0]
            print(f"\n🏆 最终匹配：【{top['name']}】")
            print(f"匹配得分：{top['score']}")
            print(f"推荐理由：{top['desc']}")
            
            if len(results) > 1:
                print("\n其他合格的备选方案：")
                for r in results[1:3]:
                    print(f"- {r['name']} (匹配分: {r['score']})")

if __name__ == "__main__":
    matcher = ClawSecurityMatch()
    matcher.run_quiz()
