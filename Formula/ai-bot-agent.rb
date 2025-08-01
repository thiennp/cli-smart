class AiBotAgent < Formula
  desc "🤖 AI Bot Agent - Intelligent command line assistant"
  homepage "https://github.com/thiennp/cli-smart"
  url "https://github.com/thiennp/cli-smart/archive/refs/tags/v1.1.0.tar.gz"
  sha256 "PLACEHOLDER_SHA256"
  license "MIT"
  head "https://github.com/thiennp/cli-smart.git", branch: "main"

  depends_on "python@3.8"

  def install
    # Install Python dependencies
    system "python3", "-m", "pip", "install", "--prefix=#{libexec}", "."
    
    # Create the ai command script
    (bin/"ai").write <<~EOS
      #!/bin/bash
      exec "#{libexec}/bin/ai-bot" "$@"
    EOS
    
    # Make the script executable
    chmod 0755, bin/"ai"
  end

  test do
    # Test that the ai command is available
    system "#{bin}/ai", "--help"
  end
end 