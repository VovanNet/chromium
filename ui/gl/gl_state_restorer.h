// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef UI_GL_GL_STATE_RESTORER_H_
#define UI_GL_GL_STATE_RESTORER_H_

#include "base/basictypes.h"
#include "ui/gl/gl_export.h"

namespace gpu {
namespace gles2 {
class ContextState;
}
}

namespace gfx {

// An interface for Restoring GL State.
// This will expand over time to provide an more optimizable implementation.
class GL_EXPORT GLStateRestorer {
 public:
  GLStateRestorer();
  virtual ~GLStateRestorer();

  virtual const gpu::gles2::ContextState* GetContextState() const = 0;
  virtual void RestoreState(const gpu::gles2::ContextState* previous_state) = 0;

  DISALLOW_COPY_AND_ASSIGN(GLStateRestorer);
};

}  // namespace gfx

#endif  // UI_GL_GL_STATE_RESTORER_H_
