import OpenAI from 'openai';
import fs from 'fs';

export async function ocr({
  filePath,
  apiKey = process.env.KLUSTER_API_KEY!, // read from env or param
  model = 'google/gemma-3-27b-it', // any vision model on kluster.ai
}: {
  filePath: string;
  apiKey?: string;
  model?: string;
}) {
  const openai = new OpenAI({
    apiKey,
    baseURL: 'https://api.kluster.ai/v1',
  });

  return getMarkdown({ openai, model, filePath });
}

async function getMarkdown({
  openai,
  model,
  filePath,
}: {
  openai: OpenAI;
  model: string;
  filePath: string;
}) {
  const systemPrompt = `Convert the provided image into Markdown format. Ensure that all content from the page is included, such as headers, footers, subtexts, images (with alt text if possible), tables, and any other elements.

  Requirements:
  - Output only Markdown (no extra narrative).
  - Do NOT wrap the result in code fences.
  - Capture every visible element.`;

  const imageAsBase64 = isRemote(filePath)
    ? filePath
    : `data:image/jpeg;base64,${fs.readFileSync(filePath).toString('base64')}`;

  const response = await openai.chat.completions.create({
    model,
    messages: [
      {
        role: 'user',
        content: [
          { type: 'text', text: systemPrompt },
          { type: 'image_url', image_url: { url: imageAsBase64 } },
        ],
      },
    ],
  });

  return response.choices[0].message.content!;
}

function isRemote(path: string) {
  return path.startsWith('http://') || path.startsWith('https://');
}
