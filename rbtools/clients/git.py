    name = 'Git'

            git_top = execute([self.git, "rev-parse", "--show-toplevel"],
                              ignore_errors=True).rstrip("\n")

            # Top level might not work on old git version se we use git dir
            # to find it.
            if git_top.startswith("fatal:") or not os.path.isdir(git_dir):
                git_top = git_dir

            os.chdir(os.path.abspath(git_top))
                                 'HEAD'], ignore_errors=True).strip()
        if (not self.options.repository_url and
                        if self.options.parent_branch:
                            self.upstream_branch = self.options.parent_branch
        if self.head_ref:
            short_head = self._strip_heads_prefix(self.head_ref)
            merge = execute([self.git, 'config', '--get',
                             'branch.%s.merge' % short_head],
                            ignore_errors=True).strip()
            remote = execute([self.git, 'config', '--get',
                              'branch.%s.remote' % short_head],
                             ignore_errors=True).strip()
            merge = self._strip_heads_prefix(merge)

            if remote and remote != '.' and merge:
                self.upstream_branch = '%s/%s' % (remote, merge)
        if self.options.repository_url:
            url = self.options.repository_url
        upstream_branch = (self.options.tracking or
        parent_branch = self.options.parent_branch
        head_ref = "HEAD"
        if self.head_ref:
            head_ref = self.head_ref
                                   head_ref]).strip()
            diff_lines = self.make_diff(self.merge_base, head_ref)
        if self.options.guess_summary and not self.options.summary:
            self.options.summary = s.replace('\n', ' ').strip()
        if self.options.guess_description and not self.options.description:
            self.options.description = execute(
            cmdline = [self.git, "diff", "--no-color", "--full-index",
                       "--no-ext-diff", "--ignore-submodules", "--no-renames",
                       rev_range]

            if (self.server and
                self.server.capabilities.has_capability('diffs',
                                                        'moved_files')):
                cmdline.append('-M')

            return execute(cmdline)
        head_ref = "HEAD"
        if self.head_ref:
            head_ref = self.head_ref

                                   head_ref]).strip()
            if self.options.guess_summary and not self.options.summary:
                self.options.summary = s.replace('\n', ' ').strip()
            if (self.options.guess_description and
                not self.options.description):
                self.options.description = execute(
            if self.options.guess_summary and not self.options.summary:
                self.options.summary = s.replace('\n', ' ').strip()
            if (self.options.guess_description and
                not self.options.description):
                self.options.description = execute(