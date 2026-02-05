# Banana 图像生成插件使用指南

## 功能概览

Banana 是一个 AI 图像生成插件，支持：
- **图像生成**：使用 Gemini API 生成高质量图像
- **文字叠加**：可选在生成的图像上添加文字
- **多种比例**：支持 1:1、3:4、4:3、9:16、16:9 等常用比例
- **多档清晰度**：标准 (1024px)、高清 (2K)、超清 (4K)
- **多模型选择**：Gemini 2.0 Flash / 2.5 Flash

## 参数说明

### 必填参数

| 参数名 | 类型 | 说明 |
|--------|------|------|
| `prompt` | string | 图像生成的提示词，描述你想要生成的图像内容 |

### 可选参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `aspect_ratio` | select | `1:1` | 图片比例。可选：1:1(正方形)、3:4(竖版)、4:3(横版)、9:16(竖屏)、16:9(宽屏) |
| `quality` | select | `standard` | 图像清晰度。可选：standard(1024px)、2k(高清)、4k(超清) |
| `model` | select | `gemini-2.0-flash-exp-image-generation` | 生成模型。可选：Gemini 2.0 Flash、Gemini 2.5 Flash |
| `text_overlay` | string | - | 叠加在图片上的文字，留空则不添加文字 |
| `text_position` | select | `bottom-center` | 文字位置。可选：顶部居中/左/右、居中、底部居中/左/右 |
| `text_color` | string | `#FFFFFF` | 文字颜色，十六进制格式（如 #FFFFFF 白色、#FFD700 金色） |

## 使用示例

### 示例 1：生成普通图像

```
prompt: 一只可爱的猫咪在樱花树下玩耍
aspect_ratio: 1:1
quality: standard
```

### 示例 2：生成带文字的竖版海报

```
prompt: 一张夏天海滩日落的海报，暖色调，氛围感
aspect_ratio: 3:4
quality: 2k
text_overlay: 夏日时光
text_position: bottom-center
text_color: #FFD700
```

### 示例 3：生成宽屏壁纸

```
prompt: 赛博朋克风格的城市夜景，霓虹灯光，高楼林立
aspect_ratio: 16:9
quality: 4k
```

## 提示词技巧

1. **具体描述**：包括主体、场景、风格、光线、色彩等
2. **艺术风格**：可以指定油画、水彩、赛博朋克、宫崎骏风格等
3. **光线氛围**：如 golden hour（黄金时刻）、soft lighting（柔和光线）

## 注意事项

1. 需要配置 Gemini API Key
2. 4K 质量生成时间较长，请耐心等待
3. 文字叠加功能需要 `_assets/fonts/` 目录中有中文字体
4. 建议提示词使用英文以获得更好的效果
