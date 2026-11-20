import fs from 'node:fs';
import path from 'node:path';
import type { Plugin, ResolvedConfig } from 'vite';

const contentTypes: Record<string, string> = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.mjs': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.pdf': 'application/pdf',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.webp': 'image/webp',
  '.gif': 'image/gif',
  '.ico': 'image/x-icon',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.mp3': 'audio/mpeg',
  '.mp4': 'video/mp4',
};

/** Serve and package the original static pages without routing them through the SPA. */
export function legacyArchive(): Plugin {
  let root = process.cwd();

  return {
    name: 'legacy-html-archive',
    apply: 'serve',
    configResolved(config) {
      root = config.root;
    },
    configureServer(server) {
      server.middlewares.use((req, res, next) => {
        const requestUrl = new URL(req.url ?? '/', 'http://localhost');
        if (requestUrl.searchParams.has('raw') || requestUrl.searchParams.has('import')) {
          next();
          return;
        }
        let pathname: string;
        try {
          pathname = decodeURIComponent(new URL(req.url ?? '/', 'http://localhost').pathname);
        } catch {
          res.statusCode = 400;
          res.end('Bad request');
          return;
        }

        if (pathname !== '/legacy_html' && !pathname.startsWith('/legacy_html/')) {
          next();
          return;
        }

        const archiveRoot = path.resolve(root, 'legacy_html');
        const relativePath = pathname.slice('/legacy_html'.length).replace(/^\/+/, '') || 'index.html';
        const target = path.resolve(archiveRoot, relativePath.endsWith('/') ? `${relativePath}index.html` : relativePath);
        if (target !== archiveRoot && !target.startsWith(`${archiveRoot}${path.sep}`)) {
          res.statusCode = 403;
          res.end('Forbidden');
          return;
        }
        if (!fs.existsSync(target) || !fs.statSync(target).isFile()) {
          res.statusCode = 404;
          res.end('Not found');
          return;
        }

        res.statusCode = 200;
        res.setHeader('Content-Type', contentTypes[path.extname(target).toLowerCase()] ?? 'application/octet-stream');
        res.setHeader('Cache-Control', 'no-cache');
        if (req.method === 'HEAD') {
          res.end();
          return;
        }
        fs.createReadStream(target).pipe(res);
      });
    },
  };
}

/** Copy the self-contained archive verbatim rather than building its HTML as SPA entries. */
export function legacyArchiveBuild(): Plugin {
  let config: ResolvedConfig;
  return {
    name: 'legacy-html-archive-build',
    apply: 'build',
    configResolved(resolved) {
      config = resolved;
    },
    closeBundle() {
      const outputDir = path.resolve(config.root, config.build.outDir);
      fs.cpSync(path.resolve(config.root, 'legacy_html'), path.join(outputDir, 'legacy_html'), {
        recursive: true,
      });
    },
  };
}
