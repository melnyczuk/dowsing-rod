import { createWriteStream } from 'fs';

export const saveFile = 
  (path: string, filename: string, ext: string) => 
    (result: any, i: number): void => 
      result.pipe(createWriteStream(`${path}/${filename}:${i}.${ext}`));

// export const download = (data: BlobPart, filename: string, type: BlobPropertyBag['type']): void => {
//   const file = new Blob([data], { type });
//   const href = URL.createObjectURL(file);

//   const a = document.createElement('a', { href, download: filename } as ElementCreationOptions);
//   document.body.appendChild(a);

//   a.click();
  
//   setTimeout(function() {
//     document.body.removeChild(a);
//     window.URL.revokeObjectURL(href);
//   }, 0);
// }
      
